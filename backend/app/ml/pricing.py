from fastapi import APIRouter, Query

router = APIRouter(prefix="/ml", tags=["ML"])


@router.get("/price-prediction")
async def get_price_prediction(
    commodity: str = Query("Cotton Yarn", description="Commodity name"),
):
    """Mock time-series forecasting — predicts raw material price direction."""
    predictions = {
        "Cotton Yarn": {
            "commodity": "Cotton Yarn",
            "current_price": "₹245/kg",
            "predicted_direction": "up",
            "predicted_change": "+8-12%",
            "confidence": 87,
            "timeframe": "next 7 days",
            "recommendation": (
                "Buy Cotton Yarn Now — Prices expected to rise by 8–12% next week "
                "due to reduced supply from Gujarat mills."
            ),
        },
        "Mulberry Silk": {
            "commodity": "Mulberry Silk",
            "current_price": "₹4,200/kg",
            "predicted_direction": "up",
            "predicted_change": "+3-5%",
            "confidence": 72,
            "timeframe": "next 14 days",
            "recommendation": "Mulberry Silk prices stable but expected to rise moderately.",
        },
    }
    return predictions.get(commodity, {
        "commodity": commodity,
        "current_price": "N/A",
        "predicted_direction": "stable",
        "predicted_change": "0%",
        "confidence": 50,
        "timeframe": "next 7 days",
        "recommendation": f"No specific prediction available for {commodity}.",
    })
