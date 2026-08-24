from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.environ.get("GOOGLE_API_KEY")

for model in ["models/embedding-001", "models/text-embedding-004", "embedding-001", "text-embedding-004"]:
    print(f"Testing {model}...")
    try:
        emb = GoogleGenerativeAIEmbeddings(model=model, google_api_key=api_key)
        res = emb.embed_query("hello")
        print(f"SUCCESS: {model} (len: {len(res)})")
        break
    except Exception as e:
        print(f"FAILED: {e}")
