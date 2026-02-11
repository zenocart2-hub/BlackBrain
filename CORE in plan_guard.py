"""
Plan Guard
----------
Controls access based on user's subscription plan.
"""

from fastapi import HTTPException, status

# ----------------------------------------
# FEATURE ACCESS MAP
# ----------------------------------------

PLAN_FEATURES = {
    "free": [
        "basic"
    ],
    "pro_monthly": [
        "basic",
        "decision",
        "study",
        "money"
    ],
    "ultra_monthly": [
        "basic",
        "decision",
        "study",
        "money",
        "problem",
        "nobullshit"
    ],
    "yearly": [
        "all"
    ]
}


# ----------------------------------------
# PLAN CHECK FUNCTION
# ----------------------------------------

def check_plan_access(
    user_plan: str,
    requested_mode: str
):
    """
    Raises error if plan does not allow requested feature
    """
    allowed_features = PLAN_FEATURES.get(user_plan)

    if not allowed_features:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid subscription plan"
        )

    if "all" in allowed_features:
        return True

    if requested_mode not in allowed_features:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Upgrade your plan to access this feature"
        )

    return True