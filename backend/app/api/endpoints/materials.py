from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.material import CommodityRead, MandiComparisonRead
from app.crud.material import list_commodities, get_mandi_comparison

router = APIRouter()


@router.get("/commodities", response_model=list[CommodityRead])
async def get_commodities(db: AsyncSession = Depends(get_db)):
    """Get all commodity price cards."""
    commodities = await list_commodities(db)
    return commodities


@router.get("/mandi", response_model=list[MandiComparisonRead])
async def get_mandi(
    category: str = Query("Textiles", description="Category: Textiles or Metals"),
    db: AsyncSession = Depends(get_db),
):
    """Get local mandi comparison data for a given category."""
    comparison = await get_mandi_comparison(db, category)
    return comparison
