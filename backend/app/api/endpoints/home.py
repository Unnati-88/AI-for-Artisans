from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
async def get_dashboard():
    """Aggregated dashboard data — mock JSON matching Home.jsx."""
    return {
        "greeting": {
            "title": "Namaste, Ramesh ji",
            "subtitle": "Here is your plan for Tuesday, 14 Oct",
            "next_market": "in 2 Days",
        },
        "priority_action": {
            "badge": "PRIORITY ACTION",
            "title": "Start Weaving for Diwali Stock",
            "title_hi": "दिवाली स्टॉक के लिए बुनाई शुरू करें",
            "description": (
                "Market demand for festive red & gold sarees is peaking. If you start "
                "today, you will catch the prime selling window next week."
            ),
            "image_url": "/images/loom_weaving.png",
        },
        "insights": [
            {
                "type": "cost_saving",
                "label": "COST SAVING",
                "title": "Cotton Yarn Price Drop",
                "description": "Down 15% in Jaipur Mandi today.",
                "action_text": "Buy Bulk Now",
                "action_text_hi": "बड़ी खरीदारी करें",
                "link": "/constraints",
            },
            {
                "type": "design_trend",
                "label": "DESIGN TREND",
                "title": "Peacock Motifs",
                "description": "High demand in upcoming wedding season.",
                "action_text": "View 3 Patterns",
                "action_text_hi": "3 डिज़ाइन देखें",
                "link": "/trends",
            },
            {
                "type": "operations",
                "label": "OPERATIONS",
                "title": "Humidity Alert",
                "description": "High humidity may affect dyeing process.",
                "action_text": "Dry Indoors",
                "action_text_hi": "अंदर सुखाएं",
                "link": "/production-advisor",
            },
        ],
    }
