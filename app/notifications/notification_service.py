import logging

logger = logging.getLogger(__name__)


def send_notification(user_id: int, message: str) -> bool:
    try:
        _dispatch(user_id, message)
        return True
    except ConnectionError:
        logger.error("Notification delivery failed", extra={"user_id": user_id})
        return False


def _dispatch(user_id: int, message: str) -> None:
    # Placeholder for the real provider call (email/SMS/push).
    pass
