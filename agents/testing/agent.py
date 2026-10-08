import json
from google import genai

from core.config.settings import settings


MODEL_NAME = "gemini-2.5-flash"


def clean_gemini_response(response):
    """
    Safely extract text from Gemini response.
    """

    if response is None:
        raise ValueError("Gemini returned an empty response.")

    text = getattr(response, "text", None)

    if text is None:
        raise ValueError("Gemini response.text is empty.")

    text = str(text).strip()

    if not text:
        raise ValueError("Gemini returned an empty response.")

    if text.startswith("```json"):
        text = text[7:]

    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def testing_agent(state):
    """
    Testing Agent:
    Analyzes generated source code and creates
    a structured testing report.
    """

    print("\n🧪 Testing Agent started...")

    generated_files = state.get("generated_files", {})

    if not generated_files:

        print("❌ No generated files available for testing.")

        return {
            **state,
            "status": "error",
            "errors": state.get("errors", []) + [
                "No generated files available for testing."
            ]
        }

    print("🔍 Analyzing generated source code with Gemini...")

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    prompt = f"""
You are the Testing Agent of DevForge AI.

Analyze the following generated software project.

GENERATED FILES:
{json.dumps(generated_files, indent=2)}

Create a detailed testing report.

Return ONLY valid JSON in exactly this structure:

{{
    "overall_status": "PASS or FAIL",
    "summary": "Short summary of testing",
    "test_cases": [
        {{
            "id": "TC001",
            "name": "Test name",
            "priority": "High/Medium/Low",
            "status": "PASS/FAIL",
            "description": "What is being tested",
            "expected": "Expected behavior",
            "actual": "Observed behavior"
        }}
    ],
    "issues": [
        {{
            "severity": "High/Medium/Low",
            "file": "file path",
            "issue": "Description of issue"
        }}
    ],
    "passed_checks": [],
    "failed_checks": [],
    "recommendations": []
}}

IMPORTANT:
1. Analyze the actual generated files.
2. Identify realistic software issues.
3. If important issues exist, overall_status must be FAIL.
4. If no important issues exist, overall_status must be PASS.
5. Return valid JSON only.
6. Do not use markdown code fences.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        print("📥 Testing response received.")

        result = clean_gemini_response(response)

        print(
            f"📏 Response length: {len(result)} characters"
        )

        # ----------------------------------------
        # Parse JSON
        # ----------------------------------------

        try:

            test_report = json.loads(result)

        except json.JSONDecodeError:

            print(
                "⚠️ Direct JSON parsing failed. "
                "Attempting recovery..."
            )

            start = result.find("{")
            end = result.rfind("}")

            if start == -1 or end == -1:

                raise ValueError(
                    "Gemini did not return valid JSON."
                )

            test_report = json.loads(
                result[start:end + 1]
            )

        # ----------------------------------------
        # Validate report
        # ----------------------------------------

        if not isinstance(test_report, dict):

            raise ValueError(
                "Testing report must be a JSON object."
            )

        test_cases = test_report.get(
            "test_cases",
            []
        )

        issues = test_report.get(
            "issues",
            []
        )

        passed_checks = test_report.get(
            "passed_checks",
            []
        )

        failed_checks = test_report.get(
            "failed_checks",
            []
        )

        recommendations = test_report.get(
            "recommendations",
            []
        )

        overall_status = str(
            test_report.get(
                "overall_status",
                "FAIL"
            )
        ).upper()

        # ----------------------------------------
        # Normalize status
        # ----------------------------------------

        if overall_status not in ["PASS", "FAIL"]:

            overall_status = "FAIL"

        test_report["overall_status"] = overall_status

        test_report["test_cases"] = test_cases

        test_report["issues"] = issues

        test_report["passed_checks"] = passed_checks

        test_report["failed_checks"] = failed_checks

        test_report["recommendations"] = recommendations

        # ----------------------------------------
        # Test Results
        # ----------------------------------------

        test_results = []

        for test_case in test_cases:

            if isinstance(test_case, dict):

                test_results.append(
                    {
                        "id": test_case.get("id"),
                        "name": test_case.get("name"),
                        "status": test_case.get(
                            "status",
                            "UNKNOWN"
                        ),
                        "priority": test_case.get(
                            "priority",
                            "Medium"
                        )
                    }
                )

        # ----------------------------------------
        # Activity Log
        # ----------------------------------------

        activity_log = state.get(
            "activity_log",
            []
        )

        activity_log.append(
            "Testing Agent analyzed generated "
            "code and created a testing report"
        )

        # ----------------------------------------
        # Final Output
        # ----------------------------------------

        print("\n✅ Testing Agent completed.")

        print(
            f"🧪 Test cases generated: "
            f"{len(test_cases)}"
        )

        print(
            f"📊 Overall Test Status: "
            f"{overall_status}"
        )

        print(
            f"❌ Issues found: "
            f"{len(issues)}"
        )

        print(
            f"✅ Passed checks: "
            f"{len(passed_checks)}"
        )

        print(
            f"⚠️ Failed checks: "
            f"{len(failed_checks)}"
        )

        print(
            f"💡 Recommendations: "
            f"{len(recommendations)}"
        )

        return {
            **state,

            # IMPORTANT:
            # Save complete testing report
            "testing_report": test_report,

            # Save simplified test results
            "test_results": test_results,

            # Save status for LangGraph
            "status": "testing_completed",

            # Save current agent
            "current_agent": "testing_agent",

            # Save activity
            "activity_log": activity_log
        }

    # ----------------------------------------
    # Gemini / API errors
    # ----------------------------------------

    except Exception as e:

        error_message = str(e)

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
        ):

            error_message = (
                "Gemini API quota exceeded. "
                "Please retry later."
            )

        elif (
            "503" in error_message
            or "UNAVAILABLE" in error_message
        ):

            error_message = (
                "Gemini service is temporarily "
                "unavailable. Please retry later."
            )

        print(
            f"\n❌ Testing Agent error: "
            f"{error_message}"
        )

        return {
            **state,

            "status": "error",

            "current_agent": "testing_agent",

            "errors": state.get(
                "errors",
                []
            ) + [
                error_message
            ]
        }