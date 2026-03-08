from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from app.db.base import Base


class Order(Base):
    """Order model — specified in Blueprint §6.2."""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    artisan_id = Column(Integer, ForeignKey("artisans.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(String(50), default="₹0")
    status = Column(String(20), default="pending")  # pending, fulfilled, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())
