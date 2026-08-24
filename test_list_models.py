import os
from google import genai
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

try:
    for m in client.models.list():
        if "embed" in m.name.lower():
            print(f"Embedding Model: {m.name}")
except Exception as e:
    print(f"FAILED: {e}")
