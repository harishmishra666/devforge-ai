import json

from google import genai

from core.config.settings import settings
from core.state.agent_state import DevForgeState


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

    # Remove markdown JSON fences
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def architect_agent(state: DevForgeState):
    """
    Architect Agent:

    Converts the project plan into a technical system architecture.
    """

    print("\n🏗️ Architect Agent started...")

    project_plan = state.get("project_plan", {})

    # ----------------------------------------
    # Validate project plan
    # ----------------------------------------

    if not project_plan:
        error_message = (
            "No project plan is available "
            "for architecture design."
        )

        print(f"❌ {error_message}")

        errors = state.get("errors", []).copy()
        errors.append(error_message)

        activity_log = state.get("activity_log", []).copy()
        activity_log.append(
            "Architect Agent failed: project plan unavailable."
        )

        return {
            **state,
            "architecture": {},
            "current_agent": "architect_agent",
            "status": "architecture_failed",
            "errors": errors,
            "activity_log": activity_log,
        }

    try:

        # ----------------------------------------
        # Gemini client
        # ----------------------------------------

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        # ----------------------------------------
        # Architecture prompt
        # ----------------------------------------

        prompt = f"""
You are the Architect Agent of DevForge AI.

Your job is to convert the project plan into a clear,
professional and implementation-ready technical architecture.

PROJECT PLAN:
{json.dumps(project_plan, indent=2)}

Design the architecture carefully.

Return ONLY valid JSON in this exact structure:

{{
    "architecture_summary": "Short description of the overall architecture",
    "architecture_pattern": "Architecture pattern used",
    "frontend": {{
        "technology": "Frontend technology",
        "components": []
    }},
    "backend": {{
        "technology": "Backend technology",
        "components": []
    }},
    "database": {{
        "technology": "Database technology",
        "tables": []
    }},
    "apis": [],
    "ai_components": [],
    "external_services": [],
    "project_structure": [],
    "data_flow": [],
    "security": [],
    "deployment": {{
        "platform": "",
        "method": ""
    }},
    "dependencies": []
}}

IMPORTANT:
1. Return valid JSON only.
2. Do not use markdown code fences.
3. Make the architecture practical and implementation-ready.
4. Select technologies appropriate for the project.
5. Keep the architecture consistent with the project plan.
6. Do not invent unnecessary technologies.
"""

        # ----------------------------------------
        # Gemini request
        # ----------------------------------------

        print("🧠 Creating technical architecture with Gemini...")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        print("📥 Architect response received.")

        result = clean_gemini_response(response)

        print(
            f"📄 Response length: {len(result)} characters"
        )

        # ----------------------------------------
        # Parse JSON
        # ----------------------------------------

        try:

            architecture = json.loads(result)

        except json.JSONDecodeError:

            print(
                "⚠️ Direct JSON parsing failed. "
                "Attempting recovery..."
            )

            start = result.find("{")
            end = result.rfind("}")

            if start == -1 or end == -1:
                raise ValueError(
                    "Gemini did not return valid architecture JSON."
                )

            architecture = json.loads(
                result[start:end + 1]
            )

        # ----------------------------------------
        # Validate architecture
        # ----------------------------------------

        if not isinstance(architecture, dict):
            raise ValueError(
                "Architect response must be a JSON object."
            )

        # ----------------------------------------
        # Activity log
        # ----------------------------------------

        activity_log = state.get(
            "activity_log",
            []
        ).copy()

        activity_log.append(
            "Architect Agent completed technical architecture design."
        )

        # ----------------------------------------
        # Final output
        # ----------------------------------------

        print("\n✅ Architect Agent completed.")

        return {
            **state,
            "architecture": architecture,
            "current_agent": "architect_agent",
            "status": "architecture_completed",
            "activity_log": activity_log,
        }

    # ----------------------------------------
    # Error handling
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

        print(f"\n❌ Architect Agent error: {error_message}")

        errors = state.get(
            "errors",
            []
        ).copy()

        errors.append(error_message)

        activity_log = state.get(
            "activity_log",
            []
        ).copy()

        activity_log.append(
            f"Architect Agent failed: {error_message}"
        )

        return {
            **state,
            "architecture": {},
            "current_agent": "architect_agent",
            "status": "architecture_failed",
            "errors": errors,
            "activity_log": activity_log,
        }