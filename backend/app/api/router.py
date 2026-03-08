from fastapi import APIRouter

from app.api.endpoints import auth, artisans, products, orders, materials, trends, home, production
from app.ml import pricing as ml_pricing, trends as ml_trends, description_generator as ml_description

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(artisans.router, prefix="/artisans", tags=["Artisans"])
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(materials.router, prefix="/materials", tags=["Materials"])
api_router.include_router(trends.router, prefix="/trends", tags=["Trends"])
api_router.include_router(home.router, prefix="/home", tags=["Home"])
api_router.include_router(production.router, prefix="/production", tags=["Production"])

# ML Mock Services (Blueprint §6.3)
api_router.include_router(ml_pricing.router)
api_router.include_router(ml_trends.router)
api_router.include_router(ml_description.router)

