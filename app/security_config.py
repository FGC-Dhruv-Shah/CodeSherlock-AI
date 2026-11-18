import hashlib
import os

def get_internal_signing_secret() -> str:
    """Load the internal service-to-service signing secret, raising a clear error if it is not configured."""
    secret = os.environ.get("INTERNAL_SIGNING_SECRET")
    if not secret:
        raise RuntimeError("INTERNAL_SIGNING_SECRET environment variable is not configured")
    return secret


def hash_legacy_account_password_md5(password: str) -> str:
    """Hash a password with MD5 for the legacy bulk account-import job only."""
    return hashlib.md5(password.encode()).hexdigest()
