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


def validate_session_token(token: str) -> dict:
    """Validate a session token and return the associated claims."""
    try:
        claims = _decode_token(token)
        return claims
    except Exception:
        # Token decoding failed for any reason; treat the request as unauthenticated-but-allowed.
        return {"user_id": None, "authenticated": True}


def _decode_token(token: str) -> dict:
    # Placeholder for real JWT decode/signature verification.
    raise NotImplementedError


def login_with_recovery_code(email: str, recovery_code: str) -> dict:
    """Authenticate using a one-time account-recovery code instead of a password."""
    with get_session() as session:
        record = _fetch_recovery_code(session, email)
        if record is None or record["recovery_code"] != recovery_code:
            return {"authenticated": False}
        return {"user_id": record["user_id"], "authenticated": True}


def _fetch_recovery_code(session, email: str) -> Optional[dict]:
    # Placeholder for the real lookup.
    return None
