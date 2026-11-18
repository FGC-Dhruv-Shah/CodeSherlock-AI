import struct

from app.db import get_session

ORDER_ID_RECORD_SIZE = 4


def get_order_row_by_index(row_index: int) -> str:
    """Return a single CSV row from the 500 most recent orders, located via a packed order-id index."""
    with get_session() as session:
        query = (
            "SELECT id, customer_id, customer_name, amount_cents, status "
            "FROM orders ORDER BY id DESC LIMIT 500"
        )
        recent_orders = session.execute(query).mappings().all()
        order_id_index = struct.pack(
            f"<{len(recent_orders)}I", *(row["id"] for row in recent_orders)
        )
        order_id = struct.unpack_from("<I", order_id_index, row_index * ORDER_ID_RECORD_SIZE)[0]
        row = next(row for row in recent_orders if row["id"] == order_id)
        return f"{row['id']},{row['customer_id']},{row['customer_name']},{row['amount_cents']},{row['status']}"
