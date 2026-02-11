"""
Subscription Routes
-------------------
- Create Razorpay order
- Verify payment & activate plan
- Get current subscription status
"""

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime

from core.security import get_current_user
from core.payment import (
    create_payment_order,
    verify_and_activate_payment
)
from core.config import SUBSCRIPTION_PLANS
from db.mongo import users
from db.models import CreateOrderRequest, VerifyPaymentRequest

router = APIRouter()

# ----------------------------------------
# GET AVAILABLE PLANS
# ----------------------------------------
@router.get("/plans")
async def get_plans():
    """
    Returns all available subscription plans
    """
    plans = []
    for code, info in SUBSCRIPTION_PLANS.items():
        plans.append({
            "plan_code": code,
            "price": info.get("price", 0),
            "duration_days": info.get("duration_days"),
            "features": info.get("features", [])
        })
    return {"plans": plans}


# ----------------------------------------
# CREATE PAYMENT ORDER
# ----------------------------------------
@router.post("/create-order")
async def create_order(
    data: CreateOrderRequest,
    current_user=Depends(get_current_user)
):
    """
    Creates Razorpay order for selected plan
    """
    user_id = current_user["user_id"]
    plan_code = data.plan_code

    order = create_payment_order(plan_code, user_id)
    return order


# ----------------------------------------
# VERIFY PAYMENT & ACTIVATE PLAN
# ----------------------------------------
@router.post("/verify")
async def verify_payment(
    data: VerifyPaymentRequest,
    current_user=Depends(get_current_user)
):
    """
    Verifies Razorpay payment and activates subscription
    """
    user_id = current_user["user_id"]

    result = await verify_and_activate_payment(
        user_id=user_id,
        plan_code=data.plan_code,
        razorpay_payment_id=data.razorpay_payment_id,
        razorpay_order_id=data.razorpay_order_id,
        razorpay_signature=data.razorpay_signature
    )

    return result


# ----------------------------------------
# GET CURRENT SUBSCRIPTION STATUS
# ----------------------------------------
@router.get("/status")
async def subscription_status(
    current_user=Depends(get_current_user)
):
    """
    Returns user's current plan & validity
    """
    user = await users.find_one({"_id": current_user["user_id"]})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "plan": user.get("plan", "free"),
        "payment_status": user.get("payment_status", "free"),
        "plan_expiry": user.get("plan_expiry")
    }