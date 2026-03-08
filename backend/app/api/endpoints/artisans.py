from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.api.dependencies import get_current_user
from app.models.artisan import Artisan
from app.schemas.artisan import ArtisanRead, ArtisanUpdate
from app.crud.artisan import update_artisan

router = APIRouter()


@router.get("/me", response_model=ArtisanRead)
async def get_my_profile(current_user: Artisan = Depends(get_current_user)):
    """Get the current artisan's full profile."""
    return current_user


@router.patch("/me", response_model=ArtisanRead)
async def update_my_profile(
    updates: ArtisanUpdate,
    current_user: Artisan = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update the current artisan's profile."""
    updated = await update_artisan(db, current_user, updates.model_dump(exclude_unset=True))
    return updated
