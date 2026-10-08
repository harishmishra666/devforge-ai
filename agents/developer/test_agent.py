from agents.developer.agent import developer_agent


test_state = {
    "user_requirement": "Build an AI-powered task management application",

    "architecture": {
        "architecture_overview": (
            "A modular client-server architecture with React frontend, "
            "FastAPI backend and PostgreSQL database."
        ),

        "architecture_style": "Layered and Modular",

        "frontend": {
            "technology": "React",
            "components": [
                "Login",
                "Register",
                "Dashboard",
                "Task List"
            ]
        },

        "backend": {
            "technology": "Python FastAPI",
            "components": [
                "Authentication",
                "User Management",
                "Task Management",
                "AI Prioritization"
            ]
        },

        "database": {
            "technology": "PostgreSQL",
            "tables": [
                "users",
                "tasks"
            ]
        },

        "api_design": [
            {
                "endpoint": "/api/auth/register",
                "method": "POST",
                "purpose": "Register a new user"
            },
            {
                "endpoint": "/api/auth/login",
                "method": "POST",
                "purpose": "Authenticate user"
            },
            {
                "endpoint": "/api/tasks",
                "method": "GET",
                "purpose": "Get user tasks"
            },
            {
                "endpoint": "/api/tasks",
                "method": "POST",
                "purpose": "Create a task"
            }
        ],

        "project_structure": [
            "backend/app/main.py",
            "backend/app/core/config.py",
            "backend/app/api/auth.py",
            "backend/app/api/tasks.py",
            "frontend/",
            "docker-compose.yml"
        ],

        "data_flow": [
            "User accesses React frontend",
            "Frontend communicates with FastAPI",
            "FastAPI stores data in PostgreSQL"
        ],

        "security": [
            "JWT authentication",
            "Password hashing",
            "Environment variables"
        ],

        "deployment": {
            "technology": "Docker",
            "components": [
                "Backend container",
                "Frontend container",
                "PostgreSQL container"
            ]
        }
    },

    "generated_files": {},
    "activity_log": [],
    "errors": []
}


print("\n🚀 Testing DevForge AI Developer Agent")
print("=" * 55)


result = developer_agent(test_state)


print("\n" + "=" * 55)
print("👨‍💻 Developer Agent Result")
print("=" * 55)

print("Status:", result.get("status"))
print("Current Agent:", result.get("current_agent"))

generated_files = result.get("generated_files", {})

print("\n📁 Generated Files:")

for file_path, content in generated_files.items():

    print("\n" + "-" * 55)
    print("📄", file_path)
    print("-" * 55)

    print(content[:500])

    if len(content) > 500:
        print("...")

print("\n📊 Total Files Generated:", len(generated_files))

print("\nActivity Log:")

for activity in result.get("activity_log", []):
    print("-", activity)

print("\nErrors:")

for error in result.get("errors", []):
    print("-", error)

print("\n✅ Developer Agent Test Completed")