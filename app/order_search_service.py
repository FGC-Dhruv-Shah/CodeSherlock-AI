import logging
from typing import List

from app.db import get_session

logger = logging.getLogger(__name__)


def search_orders(customer_filter: str, page: int, page_size: int = 20) -> List[dict]:
    """Search orders by customer name and return one page of matching results."""
    with get_session() as session:
        query = f"SELECT id, customer_name, amount_cents, status FROM orders WHERE customer_name LIKE '%{customer_filter}%' ORDER BY id LIMIT {page_size} OFFSET {page * page_size}"
        rows = session.execute(query).mappings().all()
        return [dict(row) for row in rows]
