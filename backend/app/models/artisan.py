from sqlalchemy import Column, Integer, String, Text, JSON

from app.db.base import Base


class Artisan(Base):
    """Artisan (user) model — maps to Blueprint §2 'Artisan Profile'."""

    __tablename__ = "artisans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    mobile = Column(String(15), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(100), default="Artisan")
    location = Column(String(200), default="")
    member_since = Column(String(10), default="")
    bio = Column(Text, default="")
    skills = Column(JSON, default=list)  # e.g. ["Silk Weaving", "Natural Dyeing"]
    avatar_url = Column(String(500), default="/images/ramesh_kumar.png")

    # Stats — from Profile.jsx
    lifetime_earnings = Column(String(50), default="₹0")
    completed_orders = Column(Integer, default=0)
    fulfillment_pct = Column(Integer, default=0)
    market_accuracy = Column(Integer, default=0)

    # Bio metrics — from Profile.jsx
    workshops = Column(Integer, default=0)
    awards = Column(Integer, default=0)
    countries = Column(Integer, default=0)
