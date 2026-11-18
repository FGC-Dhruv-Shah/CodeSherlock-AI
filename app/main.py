from fastapi import FastAPI

from app.auth.auth_service import login_with_recovery_code, validate_session_token
from app.auth.auth_service import router as auth_router
from app.billing.billing_service import router as billing_router
from app.order_processor import process_order
from app.order_search_service import search_orders
from app.reporting_service import get_order_row_by_index
from app.users.user_service import router as user_router

app = FastAPI(title="Customer Portal API", version="1.0.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(billing_router, prefix="/billing", tags=["billing"])


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/orders/search")
def search_orders_endpoint(customer_filter: str, page: int = 0, page_size: int = 20):
    return search_orders(customer_filter, page, page_size)


@app.post("/orders")
def create_order_endpoint(customer_id: int, items: list, promo_code: str = ""):
    return process_order(customer_id, items, promo_code)


@app.get("/reports/orders/{row_index}")
def get_order_report_row(row_index: int):
    return get_order_row_by_index(row_index)


@app.post("/auth/session/validate")
def validate_session_endpoint(token: str):
    return validate_session_token(token)


@app.post("/auth/recovery-login")
def recovery_login_endpoint(email: str, recovery_code: str):
    return login_with_recovery_code(email, recovery_code)
