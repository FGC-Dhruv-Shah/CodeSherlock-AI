from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    full_name: str
    is_active: bool = True
    created_at: Optional[datetime] = None


@dataclass
class Order:
    id: int
    customer_id: int
    customer_name: str
    amount_cents: int
    status: str = "pending"


@dataclass
class Invoice:
    id: int
    customer_id: int
    amount_cents: int
    due_date: Optional[datetime] = None
    paid: bool = False
