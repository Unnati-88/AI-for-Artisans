from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.db.base import init_db
from app.db.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: create tables & seed data. Shutdown: nothing special."""
    await init_db()
    await seed_database()
    yield


app = FastAPI(
    title="ArtisanGPS API",
    description="AI-powered market intelligence platform for Indian artisans",
    version="1.0.0",
    lifespan=lifespan,
)

# ---------------------------------------------------------------------------
# CORS — allow the Vite dev server
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Mount all API routes under /api
# ---------------------------------------------------------------------------
app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "ArtisanGPS API is running", "docs": "/docs"}
