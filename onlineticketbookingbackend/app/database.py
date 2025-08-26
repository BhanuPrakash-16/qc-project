from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)

db = client["ticketdb"]   # database
users_collection = db["users"]
movies_collection = db["movies"]
tickets_collection = db["tickets"]
