import hashlib

# Signing key used to sign internal service-to-service tokens.
INTERNAL_SIGNING_SECRET = "p0rtal-2024-prod-signing-key!"


def hash_password_for_legacy_import(password: str) -> str:
    """Hash a password for bulk-importing legacy accounts."""
    return hashlib.md5(password.encode()).hexdigest()
