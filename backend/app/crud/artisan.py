from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.artisan import Artisan
from app.core.security import hash_password, verify_password


async def get_artisan_by_mobile(db: AsyncSession, mobile: str) -> Artisan | None:
    result = await db.execute(select(Artisan).where(Artisan.mobile == mobile))
    return result.scalar_one_or_none()


async def get_artisan_by_id(db: AsyncSession, artisan_id: int) -> Artisan | None:
    result = await db.execute(select(Artisan).where(Artisan.id == artisan_id))
    return result.scalar_one_or_none()


async def create_artisan(
    db: AsyncSession,
    name: str,
    mobile: str,
    password: str,
    role: str = "Artisan",
) -> Artisan:
    artisan = Artisan(
        name=name,
        mobile=mobile,
        hashed_password=hash_password(password),
        role=role,
    )
    db.add(artisan)
    await db.flush()
    await db.refresh(artisan)
    return artisan


async def authenticate_artisan(
    db: AsyncSession, mobile: str, password: str
) -> Artisan | None:
    artisan = await get_artisan_by_mobile(db, mobile)
    if artisan is None:
        return None
    if not verify_password(password, artisan.hashed_password):
        return None
    return artisan


async def update_artisan(
    db: AsyncSession, artisan: Artisan, updates: dict
) -> Artisan:
    for key, value in updates.items():
        if value is not None:
            setattr(artisan, key, value)
    await db.flush()
    await db.refresh(artisan)
    return artisan
