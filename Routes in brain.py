"""
Brain Routes
------------
- User question receive karta hai
- Subscription plan check karta hai
- Brain engine se response generate karta hai
- History me save karta hai
"""

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime

from core.security import get_current_user
from core.plan_guard import check_plan_access
from core.brain_engine import run_brain_engine

from db.mongo import history
from db.models import BrainQuestion

router = APIRouter()

# ----------------------------------------
# ASK BRAIN
# ----------------------------------------
@router.post("/ask")
async def ask_brain(
    data: BrainQuestion,
    current_user=Depends(get_current_user)
):
    """
    Main endpoint:
    - Question
    - Mode (basic / decision / study / money / problem / nobullshit)
    """

    user_id = current_user["user_id"]
    user_plan = current_user["plan"]
    mode = data.mode

    # -----------------------------
    # PLAN ACCESS CHECK
    # -----------------------------
    check_plan_access(user_plan, mode)

    # -----------------------------
    # RUN BRAIN ENGINE
    # -----------------------------
    try:
        response = run_brain_engine(
            question=data.question,
            mode=mode
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    # -----------------------------
    # SAVE HISTORY
    # -----------------------------
    history_doc = {
        "user_id": user_id,
        "question": data.question,
        "mode": mode,
        "response": response,
        "created_at": datetime.utcnow()
    }

    await history.insert_one(history_doc)

    return {
        "question": data.question,
        "mode": mode,
        "response": response,
        "timestamp": history_doc["created_at"]
    }