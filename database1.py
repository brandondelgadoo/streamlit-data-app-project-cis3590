from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PW = os.getenv("MONGO_PW")
MONGO_CLUSTER_URL = os.getenv("MONGO_CLUSTER_URL")


FINAL_URL = (f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@{MONGO_CLUSTER_URL}/"
             "?retryWrites=true&w=majority")

client = MongoClient(FINAL_URL)
print(client)

db = client["water_quality_data"]
robot1 = db["asv_1"]

print(f"Using database {db} and collection {robot1}.")

obs1 = {"temp":92,
        "salinity":35,
        "pH":6.5,
        "oxygen":7.2,
        "notes":"good"}
result1 = robot1.insert_one(obs1)

listObs = [
    {"temp":93, "salinity":35, "pH":6.5, "oxygen":7.2, "notes":"good"},
    {"temp":94, "salinity":35, "pH":6.5, "oxygen":7.2, "notes":"good"},
    {"temp":95, "salinity":35, "pH":6.5, "oxygen":7.2, "notes":"good"}
]
result2 = robot1.insert_many(listObs)

# Other methods:

doc = robot1.find_one()

for obs in robot1.find({"temp":{"$gt":28}}): #$gt means greater than
    print("Hot water", obs)