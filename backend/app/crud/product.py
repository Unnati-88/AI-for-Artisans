from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


async def list_products(
    db: AsyncSession,
    artisan_id: int,
    search: str = "",
    category: str = "",
) -> list[Product]:
    query = select(Product).where(Product.artisan_id == artisan_id)
    if search:
        query = query.where(
            Product.name.ilike(f"%{search}%") | Product.material.ilike(f"%{search}%")
        )
    if category and category != "All Categories":
        query = query.where(Product.category == category)
    result = await db.execute(query)
    return list(result.scalars().all())


async def get_product(db: AsyncSession, product_id: int) -> Product | None:
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()


async def create_product(db: AsyncSession, artisan_id: int, data: dict) -> Product:
    product = Product(artisan_id=artisan_id, **data)
    db.add(product)
    await db.flush()
    await db.refresh(product)
    return product


async def update_product(db: AsyncSession, product: Product, updates: dict) -> Product:
    for key, value in updates.items():
        if value is not None:
            setattr(product, key, value)
    await db.flush()
    await db.refresh(product)
    return product


async def delete_product(db: AsyncSession, product: Product) -> None:
    await db.delete(product)
    await db.flush()
