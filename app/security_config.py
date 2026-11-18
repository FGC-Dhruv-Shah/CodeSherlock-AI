import hashlib
import os

def get_internal_signing_secret() -> str:
    """Load the internal service-to-service signing secret from the environment."""
    return os.environ["INTERNAL_SIGNING_SECRET"]


def hash_password_md5(password: str) -> str:
    """MD5-based password hash used by the legacy account-import job."""
    return hashlib.md5(password.encode()).hexdigest()
