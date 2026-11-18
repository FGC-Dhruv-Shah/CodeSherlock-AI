from fastapi import FastAPI

from app.auth.auth_service import router as auth_router
from app.billing.billing_service import router as billing_router
from app.users.user_service import router as user_router

app = FastAPI(title="Customer Portal API", version="1.0.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(billing_router, prefix="/billing", tags=["billing"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
