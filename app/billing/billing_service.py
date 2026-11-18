import logging

from fastapi import APIRouter

from app.db import get_session

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/invoices/{customer_id}")
def list_invoices(customer_id: int, limit: int = 20, offset: int = 0):
    limit = min(max(limit, 1), 100)
    offset = max(offset, 0)
    with get_session() as session:
        query = (
            "SELECT id, customer_id, amount_cents, paid "
            "FROM invoices WHERE customer_id = :customer_id "
            "ORDER BY id LIMIT :limit OFFSET :offset"
        )
        rows = session.execute(
            query, {"customer_id": customer_id, "limit": limit, "offset": offset}
        ).mappings().all()
        return [dict(row) for row in rows]
