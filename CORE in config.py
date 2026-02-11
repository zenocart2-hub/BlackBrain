"""
BlackBrain Core Configuration
-----------------------------
- Environment variables
- App settings
- Database config
- JWT config
- Subscription plans
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# ----------------------------------------
# LOAD ENV
# ----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)

# ----------------------------------------
# APP SETTINGS
# ----------------------------------------
APP_NAME = "BlackBrain"
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# ----------------------------------------
# SERVER
# ----------------------------------------
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

# ----------------------------------------
# DATABASE (MONGODB)
# ----------------------------------------
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"
)
MONGO_DB_NAME = os.getenv(
    "MONGO_DB_NAME",
    "blackbrain"
)

# ----------------------------------------
# JWT AUTH
# ----------------------------------------
JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "blackbrain_super_secret_key"
)
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = int(
    os.getenv("JWT_EXPIRE_MINUTES", 60 * 24)
)  # 24 hours

# ----------------------------------------
# SUBSCRIPTION PLANS
# ----------------------------------------
SUBSCRIPTION_PLANS = {
    "free": {
        "price": 0,
        "daily_limit": 5,
        "features": ["basic"]
    },
    "pro_monthly": {
        "price": 199,
        "duration_days": 30,
        "features": [
            "decision_brain",
            "study_brain",
            "creator_brain",
            "money_brain_basic",
            "no_ads"
        ]
    },
    "ultra_monthly": {
        "price": 499,
        "duration_days": 30,
        "features": [
            "decision_brain",
            "study_brain",
            "creator_brain",
            "money_brain_advanced",
            "no_bullshit_mode",
            "life_simulator",
            "business_brain",
            "priority_processing",
            "no_ads"
        ]
    },
    "yearly": {
        "price": 4999,
        "duration_days": 365,
        "features": [
            "all_features",
            "priority_processing",
            "early_access",
            "no_ads"
        ]
    }
}

# ----------------------------------------
# AI SETTINGS (FUTURE)
# ----------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")

# ----------------------------------------
# PAYMENT (RAZORPAY)
# ----------------------------------------
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "")
RAZORPAY_WEBHOOK_SECRET = os.getenv("RAZORPAY_WEBHOOK_SECRET", "")

# ----------------------------------------
# RATE LIMITS (FREE USERS)
# ----------------------------------------
FREE_DAILY_QUESTION_LIMIT = int(
    os.getenv("FREE_DAILY_QUESTION_LIMIT", 5)
)

# ----------------------------------------
# LOGGING
# ----------------------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")