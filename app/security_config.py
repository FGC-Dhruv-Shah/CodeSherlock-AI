import hashlib


def hash_legacy_account_password_md5(password: str) -> str:
    """Hash a password with MD5 for the legacy bulk account-import job only."""
    return hashlib.md5(password.encode()).hexdigest()
