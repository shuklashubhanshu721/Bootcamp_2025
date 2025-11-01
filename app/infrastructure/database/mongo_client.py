from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseModule:
    def __init__(self):
        mongo_uri = os.getenv("DATABASE_URL", "mongodb://localhost:27017/bootcamp_2025")
        try:
            self.client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
            self.db = self.client.get_database()
            # Test connection lazily
            self.client.admin.command("ping")
        except Exception as e:
            print(f"[Warning] MongoDB connection failed: {e}")
            self.client = None
            self.db = None

    def get_db(self):
        return self.db

# Create lazy singletons to prevent import-time failures
try:
    database_module = DatabaseModule()
    client = database_module.client
    db = database_module.db
except Exception as e:
    print(f"[Warning] Database module initialization failed: {e}")
    client = None
    db = None