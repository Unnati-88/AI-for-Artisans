from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    material: str = ""
    stock: int = 0
    price: str = "₹0"
    badge: str = ""
    image_url: str = ""
    category: str = "Textiles"
    description_en: str = ""
    description_hi: str = ""


class ProductRead(BaseModel):
    id: int
    artisan_id: int
    name: str
    material: str
    stock: int
    price: str
    badge: str
    image_url: str
    category: str
    description_en: str
    description_hi: str

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: str | None = None
    material: str | None = None
    stock: int | None = None
    price: str | None = None
    badge: str | None = None
    image_url: str | None = None
    category: str | None = None
    description_en: str | None = None
    description_hi: str | None = None
