from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# ----------------------------------------
# CREATE APP
# ----------------------------------------
app = FastAPI(
    title="BlackBrain",
    description="BlackBrain - Logical Problem Solving & Decision Making App",
    version="1.0.0"
)

# ----------------------------------------
# CORS (Frontend Connect)
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------
# STATIC FILES (if needed later)
# ----------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ----------------------------------------
# ROUTES IMPORT
# ----------------------------------------
from routes.auth import router as auth_router
from routes.brain import router as brain_router
from routes.subscription import router as subscription_router
from routes.history import router as history_router
from routes.settings import router as settings_router

# ----------------------------------------
# ROUTES REGISTER
# ----------------------------------------
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(brain_router, prefix="/brain", tags=["Brain"])
app.include_router(subscription_router, prefix="/subscription", tags=["Subscription"])
app.include_router(history_router, prefix="/history", tags=["History"])
app.include_router(settings_router, prefix="/settings", tags=["Settings"])

# ----------------------------------------
# ROOT ENDPOINT (TEST)
# ----------------------------------------
@app.get("/")
def root():
    return {
        "app": "BlackBrain",
        "status": "Backend running successfully 🚀",
        "message": "Think logical. Decide smart."
    }

# ----------------------------------------
# HEALTH CHECK
# ----------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}