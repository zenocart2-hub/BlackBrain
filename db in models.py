"""
Database Models (Schemas / Helpers)
----------------------------------
MongoDB ke liye logical data structure.
FastAPI + Motor ke saath use hota hai.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


# ----------------------------------------
# USER MODELS
# ----------------------------------------

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserInDB(BaseModel):
    email: EmailStr
    password: str
    plan: str = "free"
    plan_expiry: Optional[datetime] = None
    payment_status: Optional[str] = "free"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserPublic(BaseModel):
    id: str
    email: EmailStr
    plan: str
    plan_expiry: Optional[datetime]


# ----------------------------------------
# AUTH MODELS
# ----------------------------------------

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ----------------------------------------
# BRAIN / QUESTION MODELS
# ----------------------------------------

class BrainQuestion(BaseModel):
    question: str
    mode: str = "basic"  # basic / decision / study / money / problem / nobullshit


class BrainAnswer(BaseModel):
    user_id: str
    question: str
    mode: str
    response: dict
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ----------------------------------------
# HISTORY MODELS
# ----------------------------------------

class HistoryItem(BaseModel):
    user_id: str
    question: str
    mode: str
    response: dict
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ----------------------------------------
# SUBSCRIPTION MODELS
# ----------------------------------------

class CreateOrderRequest(BaseModel):
    plan_code: str


class VerifyPaymentRequest(BaseModel):
    plan_code: str
    razorpay_payment_id: str
    razorpay_order_id: str
    razorpay_signature: str


class SubscriptionPublic(BaseModel):
    plan: str
    valid_till: Optional[datetime]
    status: str


# ----------------------------------------
# SETTINGS MODELS
# ----------------------------------------

class UserSettings(BaseModel):
    language: str = "en"
    no_bullshit_mode: bool = False
    notifications: bool = True
    updated_at: datetime = Field(default_factory=datetime.utcnow)