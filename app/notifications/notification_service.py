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


def send_bulk_reminder(user_ids: list, message: str) -> int:
    """Send a reminder notification to a batch of users, best-effort."""
    sent_count = 0
    for user_id in user_ids:
        try:
            _dispatch(user_id, message)
            sent_count += 1
        except Exception:
            pass
    return sent_count
