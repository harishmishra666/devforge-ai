from agents.testing.agent import testing_agent


test_state = {
    "user_requirement": (
        "Build an AI-powered task management application "
        "where users can create, manage and prioritize tasks."
    ),

    "generated_files": {
        "backend/app/main.py": """
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevForge AI"}
""",

        "backend/app/api/auth.py": """
from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    return {"message": "Login successful"}
""",

        "backend/app/api/tasks.py": """
from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
def get_tasks():
    return []
""",

        "frontend/src/App.js": """
import React from "react";

function App() {
    return (
        <div>
            <h1>DevForge AI</h1>
        </div>
    );
}

export default App;
""",

        "backend/requirements.txt": """
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-jose
bcrypt
"""
    },

    "test_results": [],
    "activity_log": [],
    "errors": []
}


print("\n🚀 Testing DevForge AI Testing Agent")
print("=" * 60)


result = testing_agent(test_state)


print("\n" + "=" * 60)
print("🧪 Testing Agent Result")
print("=" * 60)


print("\nStatus:")
print(result.get("status"))


print("\nCurrent Agent:")
print(result.get("current_agent"))


testing_report = result.get("testing_report", {})


print("\n📊 Overall Test Status:")
print(testing_report.get("overall_status"))


print("\n📝 Summary:")
print(testing_report.get("summary"))


print("\n🧪 Test Cases:")

test_cases = testing_report.get("test_cases", [])

for test_case in test_cases:

    print("\n" + "-" * 50)

    print(
        test_case.get("id"),
        "|",
        test_case.get("name")
    )

    print("Category:", test_case.get("category"))
    print("Description:", test_case.get("description"))
    print("Expected:", test_case.get("expected_result"))
    print("Priority:", test_case.get("priority"))


print("\n❌ Issues:")

issues = testing_report.get("issues", [])

if issues:

    for issue in issues:

        print("\n" + "-" * 50)

        print("Severity:", issue.get("severity"))
        print("File:", issue.get("file"))
        print("Issue:", issue.get("issue"))
        print("Recommendation:", issue.get("recommendation"))

else:
    print("No issues identified.")


print("\n✅ Passed Checks:")

for check in testing_report.get("passed_checks", []):
    print("-", check)


print("\n❌ Failed Checks:")

for check in testing_report.get("failed_checks", []):
    print("-", check)


print("\n💡 Recommendations:")

for recommendation in testing_report.get("recommendations", []):
    print("-", recommendation)


print("\n📝 Activity Log:")

for activity in result.get("activity_log", []):
    print("-", activity)


print("\n❗ Errors:")

errors = result.get("errors", [])

if errors:

    for error in errors:
        print("-", error)

else:
    print("No errors")


print("\n" + "=" * 60)
print("🎉 Testing Agent Test Finished")
print("=" * 60)