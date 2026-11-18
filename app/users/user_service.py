import logging
from typing import Optional

from fastapi import APIRouter, HTTPException

from app.db import get_session

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{user_id}")
def get_user(user_id: int):
    with get_session() as session:
        user = _fetch_user(session, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user


def _fetch_user(session, user_id: int) -> Optional[dict]:
    query = "SELECT id, email, full_name, is_active FROM users WHERE id = :user_id"
    row = session.execute(query, {"user_id": user_id}).mappings().first()
    return dict(row) if row else None
