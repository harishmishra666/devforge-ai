import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("DevForge AI Configuration Test")
print("=" * 35)

if api_key:
    print("GEMINI_API_KEY: FOUND")
    print("API Key Length:", len(api_key))
    print("Configuration test successful!")
else:
    print("GEMINI_API_KEY: NOT FOUND")
    print("Please check your .env file.")
    