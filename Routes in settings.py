"""
History Routes
--------------
- Get user's question-answer history
- Clear complete history
"""

from fastapi import APIRouter, Depends
from core.security import get_current_user
from db.mongo import history

router = APIRouter()

# ----------------------------------------
# GET USER HISTORY
# ----------------------------------------
@router.get("/")
async def get_history(
    limit: int = 20,
    skip: int = 0,
    current_user=Depends(get_current_user)
):
    """
    Fetch logged-in user's question history
    """

    user_id = current_user["user_id"]

    cursor = (
        history
        .find({"user_id": user_id})
        .sort("created_at", -1)
        .skip(skip)
        .limit(limit)
    )

    items = []
    async for record in cursor:
        items.append({
            "id": str(record["_id"]),
            "question": record.get("question"),
            "mode": record.get("mode"),
            "response": record.get("response"),
            "created_at": record.get("created_at")
        })

    return {
        "total": len(items),
        "history": items
    }


# ----------------------------------------
# CLEAR USER HISTORY
# ----------------------------------------
@router.delete("/clear")
async def clear_history(
    current_user=Depends(get_current_user)
):
    """
    Delete all history of logged-in user
    """

    user_id = current_user["user_id"]

    result = await history.delete_many({"user_id": user_id})

    return {
        "message": "History cleared successfully",
        "deleted_count": result.deleted_count
    }