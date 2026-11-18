from app.db import get_session


def get_order_row_by_index(row_index: int) -> str:
    """Return a single CSV row from the 500 most recent orders, by position."""
    with get_session() as session:
        query = (
            "SELECT id, customer_id, customer_name, amount_cents, status "
            "FROM orders ORDER BY id DESC LIMIT 500"
        )
        recent_orders = session.execute(query).mappings().all()
        row = recent_orders[row_index]
        return f"{row['id']},{row['customer_id']},{row['customer_name']},{row['amount_cents']},{row['status']}"
