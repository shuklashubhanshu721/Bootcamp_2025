from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("DATABASE_URL", "mongodb://localhost:27017/bootcamp_2025")

print("🔍 Checking MongoDB connection using URI:", mongo_uri)

client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

try:
    info = client.server_info()
    print(f"✅ MongoDB connection successful. Version: {info['version']}")
    print("📚 Databases available:", client.list_database_names())
except Exception as e:
    print("❌ MongoDB connection failed:", e)