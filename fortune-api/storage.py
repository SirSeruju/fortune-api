from pymongo import MongoClient
import os

client = MongoClient(os.environ["MONGO_CONNECTION_STRING"])

def get_random_fortune():
    fortune = list(client.db.fortunes.aggregate([{"$sample": {"size": 1}}]))[0]
    fortune["id"] = str(fortune["_id"])
    del(fortune["_id"])
    return fortune
