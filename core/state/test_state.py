from core.state.agent_state import DevForgeState


test_state: DevForgeState = {
    "user_requirement": "Build an AI-powered task management application",
    "requirements": [
        "User authentication",
        "Task creation",
        "Task management"
    ],
    "status": "initialized",
    "current_agent": "requirement_agent",
    "activity_log": [
        "DevForge AI workflow initialized"
    ]
}


print("DevForge AI State Test")
print("----------------------")
print("Requirement:", test_state["user_requirement"])
print("Status:", test_state["status"])
print("Current Agent:", test_state["current_agent"])
print("Requirements:", test_state["requirements"])
print("State test successful!")