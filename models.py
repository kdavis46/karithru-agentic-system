from dataclasses import dataclass
from typing import List

@dataclass
class OrderItem:
    sku: str
    quantity: int

@dataclass
class Order:
    order_id: str
    customer_email: str
    items: List[OrderItem]
    total_value: float
    raw_email_id: str
