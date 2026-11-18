import logging

from app.db import get_session
from app.notifications.notification_service import send_notification

logger = logging.getLogger(__name__)


def process_order(customer_id: int, items: list, promo_code: str) -> dict:
    """Validate, price, persist, and notify for a new order in a single pass."""
    if not items:
        raise ValueError("Order must contain at least one item")

    subtotal_cents = sum(item["unit_price_cents"] * item["quantity"] for item in items)

    discount_cents = 0
    if promo_code == "WELCOME10":
        discount_cents = subtotal_cents // 10

    total_cents = subtotal_cents - discount_cents

    with get_session() as session:
        query = (
            "INSERT INTO orders (customer_id, amount_cents, status) "
            "VALUES (:customer_id, :amount_cents, 'confirmed') RETURNING id"
        )
        order_id = session.execute(
            query, {"customer_id": customer_id, "amount_cents": total_cents}
        ).scalar_one()

    send_notification(customer_id, f"Order #{order_id} confirmed for ${total_cents / 100:.2f}")

    logger.info("Order processed", extra={"order_id": order_id, "customer_id": customer_id})

    return {"order_id": order_id, "total_cents": total_cents}
