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
        raise ValueError("Gemini returned an empty text response.")

    # Remove accidental markdown JSON fences
    if text.startswith("```json"):
        text = text[7:]

    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def debugger_agent(state):
    """
    Debugger Agent:
    Analyzes testing failures and generates fixes for the
    generated source code.
    """

    print("\n🐛 Debugger Agent started...")

    generated_files = state.get("generated_files", {})
    testing_report = state.get("testing_report", {})

    if not generated_files:
        print("❌ No generated files available for debugging.")

        return {
            **state,
            "status": "error",
            "errors": state.get("errors", []) + [
                "No generated files available for debugging."
            ],
        }

    if not testing_report:
        print("❌ No testing report available for debugging.")

        return {
            **state,
            "status": "error",
            "errors": state.get("errors", []) + [
                "No testing report available for debugging."
            ],
        }

    print("🔍 Analyzing testing failures with Gemini...")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    prompt = f"""
You are the Debugger Agent of DevForge AI.

Your job is to analyze the testing report and generated source code,
identify the root cause of failures, and provide corrected source files.

TESTING REPORT:
{json.dumps(testing_report, indent=2)}

GENERATED SOURCE FILES:
{json.dumps(generated_files, indent=2)}

Analyze the issues carefully.

Return ONLY valid JSON in this exact structure:

{{
    "debug_summary": "Short summary of debugging work",
    "bugs_found": [
        {{
            "title": "Bug title",
            "severity": "High/Medium/Low",
            "root_cause": "Root cause",
            "fix": "Description of fix"
        }}
    ],
    "fixed_files": [
        {{
            "path": "relative/path/to/file.py",
            "content": "complete corrected file content"
        }}
    ],
    "remaining_issues": [],
    "recommendations": []
}}

IMPORTANT:
1. Only modify files that actually need fixing.
2. Preserve working functionality.
3. Return COMPLETE file contents for every fixed file.
4. Do not return partial code.
5. Do not use markdown code fences.
6. Return valid JSON only.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        print("📥 Debugger response received.")

        result = clean_gemini_response(response)

        print(f"📏 Response length: {len(result)} characters")

        try:
            debug_report = json.loads(result)

        except json.JSONDecodeError:
            print("⚠️ Direct JSON parsing failed. Attempting recovery...")

            start = result.find("{")
            end = result.rfind("}")

            if start == -1 or end == -1:
                raise ValueError(
                    "Gemini did not return valid JSON."
                )

            debug_report = json.loads(
                result[start:end + 1]
            )

        fixed_files = debug_report.get("fixed_files", [])

        if not isinstance(fixed_files, list):
            raise ValueError(
                "Debugger returned invalid fixed_files format."
            )

        updated_files = dict(generated_files)

        for file_data in fixed_files:

            if not isinstance(file_data, dict):
                continue

            path = file_data.get("path")
            content = file_data.get("content")

            if not path or content is None:
                continue

            updated_files[path] = content

        bugs_found = debug_report.get("bugs_found", [])
        remaining_issues = debug_report.get("remaining_issues", [])
        recommendations = debug_report.get("recommendations", [])

        print("\n✅ Debugger Agent completed.")
        print(f"🐛 Bugs found: {len(bugs_found)}")
        print(f"🔧 Files fixed: {len(fixed_files)}")
        print(f"⚠️ Remaining issues: {len(remaining_issues)}")

        activity_log = state.get("activity_log", [])

        activity_log.append(
            f"Debugger Agent completed: "
            f"{len(bugs_found)} bugs found, "
            f"{len(fixed_files)} files fixed."
        )

        return {
            **state,
            "generated_files": updated_files,
            "bugs": bugs_found,
            "debug_report": debug_report,
            "activity_log": activity_log,
            "status": "debugging_completed",
        }

    except Exception as e:

        error_message = str(e)

        print(f"❌ Debugger Agent error: {error_message}")

        return {
            **state,
            "status": "error",
            "errors": state.get("errors", []) + [
                error_message
            ],
        }