from core.orchestrator.workflow import devforge_workflow


initial_state = {
    "user_requirement": (
        "Build an AI-powered task management application "
        "where users can create, manage and prioritize tasks."
    ),

    "requirements": [],
    "project_plan": {},
    "architecture": {},
    "generated_files": {},

    "test_results": [],
    "testing_report": {},

    "bugs": [],
    "debug_report": {},

    "security_report": {},

    "github_repo": "",
    "github_url": "",

    "deployment_status": "",
    "deployment_url": "",

    "human_approval": False,

    "current_agent": "start",
    "status": "initialized",

    "activity_log": [],
    "errors": []
}


print("\n🚀 Starting DevForge AI Autonomous Workflow")
print("=" * 70)


final_state = devforge_workflow.invoke(initial_state)


print("\n" + "=" * 70)
print("✅ DevForge AI Autonomous Workflow Completed")
print("=" * 70)


# --------------------------------------------------
# Final Status
# --------------------------------------------------

print("\n🤖 Final Agent:")
print(final_state.get("current_agent"))


print("\n📊 Final Status:")
print(final_state.get("status"))


# --------------------------------------------------
# Requirements
# --------------------------------------------------

print("\n📋 Requirements:")

requirements = final_state.get("requirements", [])

print("Total Requirements:", len(requirements))

for requirement in requirements:
    print("-", requirement)


# --------------------------------------------------
# Project Plan
# --------------------------------------------------

print("\n📐 Project Plan:")

project_plan = final_state.get("project_plan", {})

print(
    "Project Goal:",
    project_plan.get("project_goal")
)

print(
    "Modules:",
    len(project_plan.get("modules", []))
)

print(
    "Development Phases:",
    len(project_plan.get("development_phases", []))
)


# --------------------------------------------------
# Architecture
# --------------------------------------------------

print("\n🏗️ Architecture:")

architecture = final_state.get("architecture", {})

print(
    "Architecture Style:",
    architecture.get("architecture_style")
)

print(
    "Frontend:",
    architecture.get("frontend", {}).get("technology")
)

print(
    "Backend:",
    architecture.get("backend", {}).get("technology")
)

print(
    "Database:",
    architecture.get("database", {}).get("technology")
)


# --------------------------------------------------
# Generated Files
# --------------------------------------------------

print("\n📁 Generated Files:")

generated_files = final_state.get("generated_files", {})

print("Total Files:", len(generated_files))

for file_path in generated_files:
    print("-", file_path)


# --------------------------------------------------
# Testing Report
# --------------------------------------------------

print("\n🧪 Final Testing Report:")

testing_report = final_state.get("testing_report", {})

print(
    "Overall Test Status:",
    testing_report.get("overall_status")
)

print(
    "Summary:",
    testing_report.get("summary")
)


# --------------------------------------------------
# Test Cases
# --------------------------------------------------

print("\n🔬 Test Cases:")

test_cases = testing_report.get("test_cases", [])

print("Total Test Cases:", len(test_cases))

for test_case in test_cases:

    print(
        f"- {test_case.get('id')}: "
        f"{test_case.get('name')} "
        f"[{test_case.get('priority')}]"
    )


# --------------------------------------------------
# Testing Issues
# --------------------------------------------------

print("\n❌ Testing Issues:")

issues = testing_report.get("issues", [])

print("Total Issues:", len(issues))

for issue in issues:

    print(
        f"- [{issue.get('severity')}] "
        f"{issue.get('file')}: "
        f"{issue.get('issue')}"
    )


# --------------------------------------------------
# Debugger Report
# --------------------------------------------------

print("\n🐛 Debugger Report:")

debug_report = final_state.get("debug_report", {})

bugs = final_state.get("bugs", [])

print(
    "Bugs Found:",
    len(bugs)
)

print(
    "Files Fixed:",
    len(debug_report.get("fixed_files", []))
)

print(
    "Remaining Issues:",
    len(debug_report.get("remaining_issues", []))
)


# --------------------------------------------------
# Debugger Details
# --------------------------------------------------

if bugs:

    print("\n🔧 Bugs Detected:")

    for bug in bugs:

        print(
            f"- [{bug.get('severity')}] "
            f"{bug.get('title')}"
        )

        print(
            "  Root Cause:",
            bug.get("root_cause")
        )

        print(
            "  Fix:",
            bug.get("fix")
        )


# --------------------------------------------------
# Activity Log
# --------------------------------------------------

print("\n📝 Activity Log:")

for activity in final_state.get("activity_log", []):

    print("-", activity)


# --------------------------------------------------
# Errors
# --------------------------------------------------

print("\n❗ Errors:")

errors = final_state.get("errors", [])

if errors:

    for error in errors:
        print("-", error)

else:

    print("No errors")


print("\n" + "=" * 70)
print("🎉 DevForge AI Autonomous Development Test Finished")
print("=" * 70)