import hashlib
import hmac
import logging
import time
from typing import Optional

from fastapi import APIRouter, HTTPException

from app.db import get_session

logger = logging.getLogger(__name__)
router = APIRouter()


def _hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000).hex()


def verify_credentials(password: str, salt: str, expected_hash: str) -> bool:
    candidate = _hash_password(password, salt)
    return hmac.compare_digest(candidate, expected_hash)


@router.post("/login")
def login(email: str, password: str):
    with get_session() as session:
        record = _fetch_user_credentials(session, email)
        if record is None or not verify_credentials(
            password, record["salt"], record["password_hash"]
        ):
            logger.warning("Failed login attempt", extra={"email": email})
            raise HTTPException(status_code=401, detail="Invalid email or password")
        logger.info("User logged in", extra={"user_id": record["user_id"]})
        return {"user_id": record["user_id"], "issued_at": int(time.time())}


def _fetch_user_credentials(session, email: str) -> Optional[dict]:
    query = "SELECT user_id, salt, password_hash FROM users WHERE email = :email"
    row = session.execute(query, {"email": email}).mappings().first()
    return dict(row) if row else None
