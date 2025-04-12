<<<<<<< HEAD
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["MindConnect"]  # <- Use the existing DB from Compass
=======
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["MindConnect"]  # <- Use the existing DB from Compass
>>>>>>> d7d969a4f396dbd6893856d16c4541fb26a331a2
