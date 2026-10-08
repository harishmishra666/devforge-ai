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


def clean_gemini_response(response):
    """
    Safely extract and clean Gemini response text.
    """

    if response is None:
        raise ValueError("Gemini returned no response.")

    result = getattr(response, "text", None)

    if result is None:
        raise ValueError(
            "Gemini response did not contain text. "
            "The model may have returned an empty or blocked response."
        )

    result = str(result).strip()

    if not result:
        raise ValueError("Gemini returned an empty response.")

    # Remove markdown code fences if Gemini adds them
    if result.startswith("```"):
        lines = result.splitlines()

        cleaned_lines = []

        for line in lines:
            line = line.strip()

            if line.startswith("```"):
                continue

            cleaned_lines.append(line)

        result = "\n".join(cleaned_lines).strip()

    return result


def developer_agent(state: DevForgeState):
    """
    Real Gemini-powered Developer Agent.

    Takes the technical architecture from the Architect Agent
    and generates the initial project source code.
    """

    architecture = state.get("architecture", {})

    if not architecture:
        error_message = "No architecture available for code generation."

        print(f"\n❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "developer_agent",
            "errors": state.get("errors", []) + [
                error_message
            ],
            "activity_log": state.get("activity_log", []) + [
                f"Developer Agent failed: {error_message}"
            ]
        }

    print("\n👨‍💻 Developer Agent started...")
    print("🧠 Generating source code with Gemini...")

    architecture_text = json.dumps(
        architecture,
        indent=2
    )

    prompt = f"""
You are the Developer Agent of DevForge AI,
an Agentic AI Software Engineering Platform.

The Architect Agent has created the following technical architecture:

{architecture_text}

Generate the initial source code for this project.

IMPORTANT:
- Generate practical, runnable code.
- Follow the architecture exactly.
- Keep the implementation modular.
- Do not generate unnecessary files.
- Every generated file must contain complete code.
- Do not generate placeholder code.
- Do not use phrases such as "add code here".
- Do not include explanations outside the JSON.

Return ONLY valid JSON using exactly this structure:

{{
    "files": [
        {{
            "path": "backend/app/main.py",
            "content": "complete source code here"
        }},
        {{
            "path": "backend/app/core/config.py",
            "content": "complete source code here"
        }}
    ]
}}

Generate the most important initial files required
to create a working project foundation.

Rules:
- Return only one JSON object.
- Do not include markdown.
- Do not include ```json.
- Do not include ```.

Return only the JSON object.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        # ----------------------------------------
        # Safely extract Gemini response
        # ----------------------------------------

        result = clean_gemini_response(response)

        print("📥 Gemini response received.")
        print(f"📏 Response length: {len(result)} characters")

        # ----------------------------------------
        # Parse JSON
        # ----------------------------------------

        try:
            generated_data = json.loads(result)

        except json.JSONDecodeError:

            # Sometimes Gemini adds extra text around JSON.
            # Try to locate the JSON object.

            start_index = result.find("{")
            end_index = result.rfind("}")

            if start_index != -1 and end_index != -1:

                json_candidate = result[
                    start_index:end_index + 1
                ]

                generated_data = json.loads(
                    json_candidate
                )

            else:
                raise ValueError(
                    "Gemini returned an invalid JSON response."
                )

        # ----------------------------------------
        # Validate generated structure
        # ----------------------------------------

        if not isinstance(generated_data, dict):

            raise ValueError(
                "Gemini response is not a JSON object."
            )

        files_data = generated_data.get("files", [])

        if not isinstance(files_data, list):

            raise ValueError(
                "Gemini response contains an invalid 'files' field."
            )

        generated_files = {}

        # ----------------------------------------
        # Extract files
        # ----------------------------------------

        for file_data in files_data:

            if not isinstance(file_data, dict):
                continue

            path = file_data.get("path")
            content = file_data.get("content")

            # Validate path
            if path is None:
                continue

            path = str(path).strip()

            if not path:
                continue

            # Validate content
            if content is None:
                continue

            content = str(content)

            if not content.strip():
                continue

            generated_files[path] = content

        # ----------------------------------------
        # Check if files were generated
        # ----------------------------------------

        if not generated_files:

            raise ValueError(
                "Gemini did not generate any valid project files."
            )

        print("\n✅ Developer Agent completed.")
        print(
            f"📁 Files generated: {len(generated_files)}"
        )

        for file_path in generated_files:
            print(f"   📄 {file_path}")

        # ----------------------------------------
        # Return updated state
        # ----------------------------------------

        return {
            "generated_files": generated_files,
            "current_agent": "developer_agent",
            "status": "code_generation_completed",
            "activity_log": state.get(
                "activity_log",
                []
            ) + [
                (
                    "Developer Agent generated "
                    f"{len(generated_files)} source files using Gemini"
                )
            ]
        }

    # --------------------------------------------
    # JSON errors
    # --------------------------------------------

    except json.JSONDecodeError as e:

        error_message = (
            "Developer Agent received invalid JSON "
            f"from Gemini: {str(e)}"
        )

        print(f"\n❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "developer_agent",
            "errors": state.get("errors", []) + [
                error_message
            ],
            "activity_log": state.get(
                "activity_log",
                []
            ) + [
                f"Developer Agent failed: {error_message}"
            ]
        }

    # --------------------------------------------
    # Gemini quota error
    # --------------------------------------------

    except Exception as e:

        error_text = str(e)

        if (
            "429" in error_text
            or "RESOURCE_EXHAUSTED" in error_text
        ):

            error_message = (
                f"Gemini API quota exceeded for "
                f"{MODEL_NAME}. "
                "Please wait for the quota reset "
                "before retrying."
            )

        elif (
            "503" in error_text
            or "UNAVAILABLE" in error_text
        ):

            error_message = (
                f"Gemini service is temporarily "
                f"unavailable for {MODEL_NAME}. "
                "Please retry later."
            )

        else:

            error_message = (
                f"Developer Agent error: {error_text}"
            )

        print(f"\n❌ {error_message}")

        return {
            "status": "error",
            "current_agent": "developer_agent",
            "errors": state.get("errors", []) + [
                error_message
            ],
            "activity_log": state.get(
                "activity_log",
                []
            ) + [
                f"Developer Agent failed: {error_message}"
            ]
        }