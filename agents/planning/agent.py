
import os
import json

from dotenv import load_dotenv
from google import genai

from core.state.agent_state import DevForgeState


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Create Gemini client
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"


def planning_agent(state: DevForgeState):
    """
    Real Gemini-powered Planning Agent.

    Takes analyzed requirements from the Requirement Agent
    and creates a structured development plan.
    """

    requirements = state.get("requirements", [])

    if not requirements:
        error_message = "No requirements available for planning."

        return {
            "status": "error",
            "current_agent": "planning_agent",
            "errors": state.get("errors", []) + [error_message],
            "activity_log": state.get("activity_log", []) + [
                f"Planning Agent error: {error_message}"
            ]
        }

    print("\n📋 Planning Agent started...")
    print("🧠 Creating development plan with Gemini...")

    requirements_text = "\n".join(
        f"{index + 1}. {requirement}"
        for index, requirement in enumerate(requirements)
    )

    prompt = f"""
You are the Planning Agent of DevForge AI,
an Agentic AI Software Engineering Platform.

The Requirement Agent has analyzed a software project
and produced the following requirements:

{requirements_text}

Create a practical software development plan based on these requirements.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "project_goal": "Short description of the project goal",
    "modules": [
        {{
            "name": "Module name",
            "description": "What this module does"
        }}
    ],
    "technologies": [
        "Technology 1",
        "Technology 2"
    ],
    "development_phases": [
        {{
            "phase": 1,
            "name": "Phase name",
            "tasks": [
                "Task 1",
                "Task 2"
            ]
        }}
    ],
    "database_requirements": [
        "Database requirement 1"
    ],
    "api_requirements": [
        "API requirement 1"
    ]
}}

Do not include markdown.
Do not include ```json.
Return only the JSON object.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        result = (response.text or "").strip()

        if not result:
            error_message = "Gemini returned an empty planning response."

            print(f"❌ {error_message}")

            return {
                "status": "error",
                "current_agent": "planning_agent",
                "errors": state.get("errors", []) + [error_message],
                "activity_log": state.get("activity_log", []) + [
                    f"Planning Agent error: {error_message}"
                ]
            }

        # Remove accidental markdown code fences
        if result.startswith("```"):
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

        project_plan = json.loads(result)

        print("\n✅ Planning Agent completed.")
        print("📋 Development plan created successfully.")

        return {
            "project_plan": project_plan,
            "current_agent": "planning_agent",
            "status": "planning_completed",
            "activity_log": state.get("activity_log", []) + [
                "Planning Agent created a development plan using Gemini"
            ],
            "errors": state.get("errors", [])
        }

    except json.JSONDecodeError as e:
        error_message = f"Planning Agent returned invalid JSON: {str(e)}"

        print(f"❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "planning_agent",
            "errors": state.get("errors", []) + [error_message],
            "activity_log": state.get("activity_log", []) + [
                f"Planning Agent error: {error_message}"
            ]
        }

    except Exception as e:
        error_message = f"Planning Agent failed: {str(e)}"

        print(f"❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "planning_agent",
            "errors": state.get("errors", []) + [error_message],
            "activity_log": state.get("activity_log", []) + [
                f"Planning Agent error: {error_message}"
            ]
        }

