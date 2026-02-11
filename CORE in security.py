"""
BlackBrain Security Module
--------------------------
Handles:
- Password hashing & verification
- JWT token creation & validation
- Current user dependency
"""

from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from bson import ObjectId

from core.config import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_EXPIRE_MINUTES
)
from db.mongo import users

# ----------------------------------------
# PASSWORD HASHING
# ----------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ----------------------------------------
# JWT CONFIG
# ----------------------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=JWT_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )
    return encoded_jwt


# ----------------------------------------
# GET CURRENT USER (DEPENDENCY)
# ----------------------------------------
async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = await users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise credentials_exception

    return {
        "user_id": str(user["_id"]),
        "email": user.get("email"),
        "plan": user.get("plan", "free"),
        "is_active": True
    }


# ----------------------------------------
# REQUIRE PAID PLAN (OPTIONAL DEPENDENCY)
# ----------------------------------------
def require_paid_plan(current=Depends(get_current_user)):
    if current.get("plan") == "free":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Upgrade plan to access this feature"
        )
    return current