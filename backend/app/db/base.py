from sqlalchemy.orm import DeclarativeBase

from app.db.session import engine


class Base(DeclarativeBase):
    """SQLAlchemy declarative base class for all models."""
    pass


async def init_db():
    """Create all database tables (if they don't already exist)."""
    # Import all models here so they are registered with Base.metadata
    import app.models.artisan  # noqa: F401
    import app.models.product  # noqa: F401
    import app.models.order  # noqa: F401
    import app.models.material  # noqa: F401

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
