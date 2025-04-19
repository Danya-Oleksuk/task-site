import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

db = None
tasks_collection = None


def create_mongo_database():
    global tasks_collection, db

    main_client = pymongo.MongoClient(os.environ.get("MONGO_API_TOKEN"))
    db = main_client["tasks_database"]

    tasks_collection = db["tasks"]


def get_tasks(user_id: int):
    lst = []

    for data in tasks_collection.find({"user_id": user_id}):
        lst.append({data.get("task"): data.get("status")})
    return lst


def count_tasks(user_id: int):
    return tasks_collection.count_documents({"user_id": user_id})
