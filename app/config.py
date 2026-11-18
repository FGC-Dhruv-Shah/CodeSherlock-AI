import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql+psycopg2://localhost/customer_portal"
    )
    jwt_secret: str = os.getenv("JWT_SECRET", "")
    environment: str = os.getenv("APP_ENV", "local")
    session_ttl_minutes: int = int(os.getenv("SESSION_TTL_MINUTES", "60"))


settings = Settings()
