from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class Material(Base):
    """Material Source model — maps to Blueprint §2 'Material Costs (Constraints)'."""

    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(String(50), default="₹0")
    unit = Column(String(20), default="/ kg")
    change_pct = Column(String(20), default="0.0%")
    trend = Column(String(10), default="flat")  # up, down, flat
    sparkline_points = Column(Text, default="")  # SVG polyline points string
    color = Column(String(20), default="#9ca3af")
    category = Column(String(50), default="Textiles")  # Textiles, Metals

    # Mandi comparison prices
    commodity_full_name = Column(String(200), default="")  # e.g. "Cotton Yarn (40s)"
    sub_unit = Column(String(50), default="Per kg")
    local_price = Column(String(50), default="")
    local_best = Column(Integer, default=0)  # 0 or 1
    surat_price = Column(String(50), default="")
    surat_best = Column(Integer, default=0)
    delhi_price = Column(String(50), default="")
    delhi_best = Column(Integer, default=0)
    action = Column(String(100), default="")  # "Source from Surat", "Buy Local"
