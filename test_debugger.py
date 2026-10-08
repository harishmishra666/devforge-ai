from agents.debugger.agent import debugger_agent


state = {
    "generated_files": {
        "backend/app/main.py": """
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello"
    }
"""
    },

    "testing_report": {
        "overall_status": "FAIL",

        "issues": [
            {
                "title": "Missing validation",
                "severity": "Medium",
                "description": "Input validation is missing."
            }
        ],

        "failed_checks": [
            "Input validation"
        ],

        "passed_checks": [
            "Application structure"
        ],

        "recommendations": [
            "Add input validation"
        ]
    },

    "activity_log": [],
    "errors": []
}


result = debugger_agent(state)


print()
print("=" * 50)
print("DEBUGGER TEST RESULT")
print("=" * 50)

print("DEBUG STATUS:", result.get("status"))
print("BUGS FOUND:", len(result.get("bugs", [])))
print("FILES FIXED:", len(result.get("generated_files", {})))
print("ERRORS:", result.get("errors", []))