from pydantic import BaseModel
from datetime import datetime


class OrderCreate(BaseModel):
    product_id: int
    quantity: int = 1
    total_price: str = "₹0"


class OrderRead(BaseModel):
    id: int
    artisan_id: int
    product_id: int
    quantity: int
    total_price: str
    status: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True


class OrderUpdate(BaseModel):
    status: str  # pending, fulfilled, cancelled
