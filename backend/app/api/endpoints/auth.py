from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from app.crud.artisan import authenticate_artisan, create_artisan, get_artisan_by_mobile
from app.core.security import create_access_token

router = APIRouter()


@router.post("/signup", response_model=TokenResponse)
async def signup(data: SignupRequest, db: AsyncSession = Depends(get_db)):
    """Create a new artisan account and return a JWT token."""
    existing = await get_artisan_by_mobile(db, data.mobile)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this mobile number already exists",
        )
    artisan = await create_artisan(db, data.name, data.mobile, data.password, data.role)
    token = create_access_token(data={"sub": str(artisan.id)})
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Authenticate an artisan and return a JWT token."""
    artisan = await authenticate_artisan(db, data.mobile, data.password)
    if artisan is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid mobile number or password",
        )
    token = create_access_token(data={"sub": str(artisan.id)})
    return TokenResponse(access_token=token)
