"""
MongoDB Connection Module (Async)
--------------------------------
- Connects to MongoDB using Motor
- Exposes database & collections
"""

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_URI, MONGO_DB_NAME

# ----------------------------------------
# CREATE MONGO CLIENT
# ----------------------------------------
client = AsyncIOMotorClient(MONGO_URI)

# ----------------------------------------
# DATABASE
# ----------------------------------------
db = client[MONGO_DB_NAME]

# ----------------------------------------
# COLLECTIONS
# ----------------------------------------
users = db["users"]
subscriptions = db["subscriptions"]
questions = db["questions"]
answers = db["answers"]
history = db["history"]
settings = db["settings"]

# ----------------------------------------
# OPTIONAL: INDEXES (SAFE TO CALL ON START)
# ----------------------------------------
async def create_indexes():
    """
    Creates important indexes for performance
    Call once on app startup if needed
    """
    await users.create_index("email", unique=True)
    await users.create_index("created_at")

    await subscriptions.create_index("user_id")
    await subscriptions.create_index("plan")

    await questions.create_index("user_id")
    await questions.create_index("created_at")

    await history.create_index("user_id")
    await history.create_index("created_at")