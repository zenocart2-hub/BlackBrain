"""
History Routes
--------------
- Get user's question-answer history
- Clear history (optional)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

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
    Returns user's question history
    Params:
    - limit: number of records
    - skip: pagination offset
    """

    user_id = current_user["user_id"]

    cursor = (
        history
        .find({"user_id": user_id})
        .sort("created_at", -1)
        .skip(skip)
        .limit(limit)
    )

    records = []
    async for item in cursor:
        records.append({
            "id": str(item["_id"]),
            "question": item.get("question"),
            "mode": item.get("mode"),
            "response": item.get("response"),
            "created_at": item.get("created_at")
        })

    return {
        "count": len(records),
        "items": records
    }


# ----------------------------------------
# CLEAR USER HISTORY
# ----------------------------------------
@router.delete("/clear")
async def clear_history(
    current_user=Depends(get_current_user)
):
    """
    Deletes all history for current user
    """

    user_id = current_user["user_id"]

    result = await history.delete_many({"user_id": user_id})

    return {
        "message": "History cleared successfully",
        "deleted_count": result.deleted_count
    }