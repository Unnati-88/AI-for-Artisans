from pydantic import BaseModel


class CommodityRead(BaseModel):
    id: int
    name: str
    price: str
    unit: str
    change_pct: str
    trend: str
    sparkline_points: str
    color: str
    category: str

    class Config:
        from_attributes = True


class MandiComparisonRead(BaseModel):
    commodity: str
    sub: str
    local_price: str
    local_best: bool
    surat_price: str
    surat_best: bool
    delhi_price: str
    delhi_best: bool
    action: str
