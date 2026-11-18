import logging

from app.db import get_session

logger = logging.getLogger(__name__)


def export_all_orders_to_csv_rows() -> list:
    """Build CSV rows for every order in the system, for the finance export report."""
    with get_session() as session:
        query = "SELECT id, customer_id, customer_name, amount_cents, status FROM orders"
        all_orders = session.execute(query).mappings().all()
        return [
            f"{row['id']},{row['customer_id']},{row['customer_name']},{row['amount_cents']},{row['status']}"
            for row in all_orders
        ]
