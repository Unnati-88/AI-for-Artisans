from fastapi import APIRouter

router = APIRouter(prefix="/ml", tags=["ML"])


@router.get("/trend-forecast")
async def get_trend_forecast():
    """Mock trend forecasting — seasonal demand predictions."""
    return {
        "season": "Diwali / Wedding Season 2024",
        "trending_motifs": [
            {"name": "Peacock Motif", "demand_change": "+40%", "regions": ["North India", "Global Export"]},
            {"name": "Lotus Pattern", "demand_change": "+35%", "regions": ["Varanasi", "Jaipur"]},
            {"name": "Floral Jaal", "demand_change": "+28%", "regions": ["Export Markets"]},
        ],
        "trending_colors": [
            {"name": "Festive Red", "hex": "#DC2626", "demand": "Very High"},
            {"name": "Royal Gold", "hex": "#F59E0B", "demand": "High"},
            {"name": "Deep Magenta", "hex": "#BE185D", "demand": "High"},
            {"name": "Ocean Blue", "hex": "#2563EB", "demand": "Moderate"},
        ],
        "recommendation": (
            "Focus on red & gold silk sarees with peacock or lotus motifs. "
            "Wedding season demand peaks in 3 weeks."
        ),
    }
