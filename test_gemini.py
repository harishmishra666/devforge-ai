from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello to DevForge AI in one short sentence."
)

print("DevForge AI Gemini Test")
print("=" * 35)
print("Gemini Response:")
print(response.text)
print("=" * 35)
print("Gemini connection successful!")