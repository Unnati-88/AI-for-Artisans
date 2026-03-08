from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.api.dependencies import get_current_user
from app.models.artisan import Artisan
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.crud.product import list_products, get_product, create_product, update_product, delete_product

router = APIRouter()


@router.get("", response_model=list[ProductRead])
async def get_products(
    search: str = Query("", description="Search by name or material"),
    category: str = Query("", description="Filter by category"),
    current_user: Artisan = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List the current artisan's products."""
    products = await list_products(db, current_user.id, search, category)
    return products


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def add_product(
    data: ProductCreate,
    current_user: Artisan = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new product for the current artisan."""
    product = await create_product(db, current_user.id, data.model_dump())
    return product


@router.patch("/{product_id}", response_model=ProductRead)
async def edit_product(
    product_id: int,
    updates: ProductUpdate,
    current_user: Artisan = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update an existing product."""
    product = await get_product(db, product_id)
    if not product or product.artisan_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    updated = await update_product(db, product, updates.model_dump(exclude_unset=True))
    return updated


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_product(
    product_id: int,
    current_user: Artisan = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete a product."""
    product = await get_product(db, product_id)
    if not product or product.artisan_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    await delete_product(db, product)
