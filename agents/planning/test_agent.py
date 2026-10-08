from agents.planning.agent import planning_agent


test_state = {
    "user_requirement": "Build an AI-powered task management application",

    "requirements": [
        "User registration",
        "User authentication",
        "Task creation",
        "Task management",
        "Task organization",
        "AI-powered task prioritization",
        "Data persistence",
        "Data security"
    ],

    "activity_log": [],
    "errors": []
}


print("\n🚀 Testing DevForge AI Planning Agent")
print("=" * 50)


result = planning_agent(test_state)


print("\n" + "=" * 50)
print("📋 Planning Agent Result")
print("=" * 50)

print("Status:", result.get("status"))
print("Current Agent:", result.get("current_agent"))

print("\nProject Plan:")

project_plan = result.get("project_plan", {})

print("\n🎯 Project Goal:")
print(project_plan.get("project_goal"))

print("\n🧩 Modules:")
for module in project_plan.get("modules", []):
    print("-", module.get("name"))
    print("  ", module.get("description"))

print("\n🔧 Technologies:")
for technology in project_plan.get("technologies", []):
    print("-", technology)

print("\n📅 Development Phases:")
for phase in project_plan.get("development_phases", []):
    print(f"\nPhase {phase.get('phase')}: {phase.get('name')}")

    for task in phase.get("tasks", []):
        print("  -", task)

print("\n🗄️ Database Requirements:")
for item in project_plan.get("database_requirements", []):
    print("-", item)

print("\n🔌 API Requirements:")
for item in project_plan.get("api_requirements", []):
    print("-", item)

print("\nActivity Log:")
for activity in result.get("activity_log", []):
    print("-", activity)

print("\n✅ Planning Agent Test Completed")