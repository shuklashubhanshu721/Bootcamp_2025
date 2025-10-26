from pymongo import MongoClient
import os

class DatabaseModule:
    def __init__(self):
        mongo_uri = os.getenv("DATABASE_URL", "mongodb://localhost:27017/bootcamp_2025")
        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_database()
    
    def get_db(self):
        return self.db

# Singleton instance for global access
database_module = DatabaseModule()