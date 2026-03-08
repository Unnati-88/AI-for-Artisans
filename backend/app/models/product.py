from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.db.base import Base


class Product(Base):
    """Product model — maps to Blueprint §2 'My Crafts (Inventory)'."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    artisan_id = Column(Integer, ForeignKey("artisans.id"), nullable=False, index=True)
    name = Column(String(200), nullable=False)
    material = Column(String(200), default="")
    stock = Column(Integer, default=0)
    price = Column(String(50), default="₹0")
    badge = Column(String(50), default="")  # "High Demand", "Stable", "Growing", "Trending"
    image_url = Column(String(500), default="")
    category = Column(String(100), default="Textiles")  # Textiles, Pottery, Jewellery, Woodwork, Metalwork
    description_en = Column(Text, default="")
    description_hi = Column(Text, default="")
