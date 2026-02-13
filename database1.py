from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PW = os.getenv("MONGO_PW")
MONGO_URL = os.getenv("MONGO_URL")
