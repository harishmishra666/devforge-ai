from agents.requirement.agent import requirement_agent


test_state = {
    "user_requirement": "Build an AI-powered task management application",
    "requirements": [],
    "activity_log": [],
    "errors": []
}


print("\n🚀 Testing DevForge AI Requirement Agent")
print("=" * 50)


result = requirement_agent(test_state)


print("\n" + "=" * 50)
print("📋 Requirement Agent Result")
print("=" * 50)

print("Status:", result.get("status"))
print("Current Agent:", result.get("current_agent"))

print("\nRequirements:")
for requirement in result.get("requirements", []):
    print("-", requirement)

print("\nActivity Log:")
for activity in result.get("activity_log", []):
    print("-", activity)

print("\n✅ Requirement Agent Test Completed")