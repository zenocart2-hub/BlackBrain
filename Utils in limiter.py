"""
Limiter Utility
---------------
- Free plan users ke liye daily question limit
- Plan-based usage control
"""

from datetime import datetime, timedelta
from fastapi import HTTPException, status

from db.mongo import history
from core.config import FREE_DAILY_QUESTION_LIMIT


# ----------------------------------------
# CHECK DAILY LIMIT FOR FREE USERS
# ----------------------------------------
async def check_daily_limit(user_id: str, user_plan: str):
    """
    Free plan users ke daily question limit ko check karta hai
    Paid users ko skip karta hai
    """

    # Paid users -> no limit
    if user_plan != "free":
        return True

    # Aaj ki date range
    today_start = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    today_end = today_start + timedelta(days=1)

    # Aaj ke questions count
    count = await history.count_documents({
        "user_id": user_id,
        "created_at": {
            "$gte": today_start,
            "$lt": today_end
        }
    })

    if count >= FREE_DAILY_QUESTION_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=(
                f"Daily free limit reached ({FREE_DAILY_QUESTION_LIMIT}). "
                "Upgrade to Pro or Ultra plan."
            )
        )

    return True