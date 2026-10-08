
import os
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


def requirement_agent(state: DevForgeState):
    """
    Real Gemini-powered Requirement Agent.

    Takes the user's software requirement,
    analyzes it using Gemini,
    and returns structured requirements.
    """

    user_requirement = state.get("user_requirement", "").strip()

    # Validate user requirement
    if not user_requirement:
        error_message = "User requirement is empty."

        return {
            "status": "error",
            "current_agent": "requirement_agent",
            "errors": state.get("errors", []) + [error_message],
            "activity_log": state.get("activity_log", []) + [
                f"Requirement Agent error: {error_message}"
            ]
        }

    print("\n🤖 Requirement Agent started...")
    print("🧠 Analyzing software requirement with Gemini...")

    prompt = f"""
You are the Requirement Analysis Agent of DevForge AI.

Analyze the following software requirement and identify the
functional and non-functional requirements.

User Requirement:
{user_requirement}

Return ONLY a numbered list of clear requirements.

Example:

1. User registration and login
2. User authentication and authorization
3. Create new tasks
4. Edit and delete tasks
5. Store task data in database
6. Responsive user interface
7. Secure API endpoints

Do not provide explanations.
Do not use markdown headings.
Only return the numbered requirements.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        response_text = (response.text or "").strip()

        # Validate Gemini response
        if not response_text:
            error_message = "Gemini returned an empty response."

            print(f"❌ {error_message}")

            return {
                "status": "error",
                "current_agent": "requirement_agent",
                "errors": state.get("errors", []) + [error_message],
                "activity_log": state.get("activity_log", []) + [
                    f"Requirement Agent error: {error_message}"
                ]
            }

        # Convert numbered response into a clean list
        requirements = []

        for line in response_text.splitlines():
            line = line.strip()

            if not line:
                continue

            # Remove common numbering formats
            cleaned = line.lstrip("0123456789.- ").strip()

            if cleaned:
                requirements.append(cleaned)

        # Fallback if parsing produced nothing
        if not requirements:
            requirements = [response_text]

        print("\n✅ Requirement analysis completed.")
        print(f"📋 Requirements identified: {len(requirements)}")

        for index, requirement in enumerate(requirements, start=1):
            print(f"{index}. {requirement}")

        return {
            "requirements": requirements,
            "status": "requirements_analyzed",
            "current_agent": "requirement_agent",
            "activity_log": state.get("activity_log", []) + [
                "Requirement Agent completed successfully."
            ],
            "errors": state.get("errors", [])
        }

    except Exception as e:
        error_message = f"Requirement Agent failed: {str(e)}"

        print(f"❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "requirement_agent",
            "errors": state.get("errors", []) + [error_message],
            "activity_log": state.get("activity_log", []) + [
                f"Requirement Agent error: {error_message}"
            ]
        }
