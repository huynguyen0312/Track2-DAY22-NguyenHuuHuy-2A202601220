from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.environ.get("GOOGLE_API_KEY")

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
    res = llm.invoke("Hello")
    print(f"SUCCESS: {res.content}")
except Exception as e:
    print(f"FAILED: {e}")
