from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.material import Material


async def list_commodities(db: AsyncSession) -> list[Material]:
    result = await db.execute(select(Material))
    return list(result.scalars().all())


async def get_mandi_comparison(db: AsyncSession, category: str = "Textiles") -> list[dict]:
    result = await db.execute(
        select(Material).where(Material.category == category)
    )
    materials = result.scalars().all()
    return [
        {
            "commodity": m.commodity_full_name or m.name,
            "sub": m.sub_unit,
            "local_price": m.local_price,
            "local_best": bool(m.local_best),
            "surat_price": m.surat_price,
            "surat_best": bool(m.surat_best),
            "delhi_price": m.delhi_price,
            "delhi_best": bool(m.delhi_best),
            "action": m.action,
        }
        for m in materials
        if m.local_price  # only include materials that have mandi data
    ]
