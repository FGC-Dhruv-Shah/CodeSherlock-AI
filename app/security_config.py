import hashlib
import os

INTERNAL_SIGNING_SECRET = os.environ["INTERNAL_SIGNING_SECRET"]


def hash_password_md5(password: str) -> str:
    """MD5-based password hash used by the legacy account-import job."""
    return hashlib.md5(password.encode()).hexdigest()
