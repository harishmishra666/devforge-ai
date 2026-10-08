from agents.architect.agent import architect_agent


test_state = {
    "user_requirement": "Build an AI-powered task management application",

    "project_plan": {
        "project_goal": "Develop an AI-powered task management platform.",

        "modules": [
            {
                "name": "Authentication & User Management",
                "description": "Handles user registration, login and profiles."
            },
            {
                "name": "Task Management",
                "description": "Handles task creation, editing, deletion and completion."
            },
            {
                "name": "AI Prioritization",
                "description": "Uses AI to prioritize tasks."
            }
        ],

        "technologies": [
            "Python",
            "FastAPI",
            "React",
            "PostgreSQL",
            "Docker"
        ],

        "development_phases": [
            {
                "phase": 1,
                "name": "Foundation",
                "tasks": [
                    "Set up backend",
                    "Create database",
                    "Implement authentication"
                ]
            },
            {
                "phase": 2,
                "name": "Core Features",
                "tasks": [
                    "Implement task management",
                    "Build frontend"
                ]
            }
        ],

        "database_requirements": [
            "Users table",
            "Tasks table"
        ],

        "api_requirements": [
            "Authentication APIs",
            "Task management APIs"
        ]
    },

    "activity_log": [],
    "errors": []
}


print("\n🚀 Testing DevForge AI Architect Agent")
print("=" * 50)


result = architect_agent(test_state)


print("\n" + "=" * 50)
print("🏗️ Architect Agent Result")
print("=" * 50)

print("Status:", result.get("status"))
print("Current Agent:", result.get("current_agent"))

architecture = result.get("architecture", {})

print("\n🏛️ Architecture Overview:")
print(architecture.get("architecture_overview"))

print("\n🏗️ Architecture Style:")
print(architecture.get("architecture_style"))

print("\n💻 Frontend:")
print(architecture.get("frontend"))

print("\n⚙️ Backend:")
print(architecture.get("backend"))

print("\n🗄️ Database:")
print(architecture.get("database"))

print("\n🔌 API Design:")
for api in architecture.get("api_design", []):
    print(
        f"- {api.get('method')} "
        f"{api.get('endpoint')} → "
        f"{api.get('purpose')}"
    )

print("\n📁 Project Structure:")
for item in architecture.get("project_structure", []):
    print("-", item)

print("\n🔄 Data Flow:")
for step in architecture.get("data_flow", []):
    print("-", step)

print("\n🔐 Security:")
for item in architecture.get("security", []):
    print("-", item)

print("\n🚀 Deployment:")
print(architecture.get("deployment"))

print("\nActivity Log:")
for activity in result.get("activity_log", []):
    print("-", activity)

print("\n✅ Architect Agent Test Completed")