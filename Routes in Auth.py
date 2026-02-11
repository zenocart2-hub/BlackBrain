"""
Auth Routes
-----------
- Signup (email + password)
- Login (JWT token)
"""

from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from datetime import datetime

from db.mongo import users
from db.models import UserCreate, TokenResponse
from core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()

# ----------------------------------------
# SIGNUP
# ----------------------------------------
@router.post("/signup", response_model=TokenResponse)
async def signup(data: UserCreate):
    # check existing user
    existing = await users.find_one({"email": data.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # create user
    user_doc = {
        "email": data.email,
        "password": hash_password(data.password),
        "plan": "free",
        "payment_status": "free",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = await users.insert_one(user_doc)
    user_id = str(result.inserted_id)

    # create JWT
    token = create_access_token({"sub": user_id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ----------------------------------------
# LOGIN
# ----------------------------------------
@router.post("/login", response_model=TokenResponse)
async def login(data: UserCreate):
    user = await users.find_one({"email": data.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": str(user["_id"])})

    # update last login
    await users.update_one(
        {"_id": ObjectId(user["_id"])},
        {"$set": {"updated_at": datetime.utcnow()}}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }