from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["expense_tracker"]
expenses_collection = db.get_collection("expenses")
budgets_collection = db.get_collection("budgets")