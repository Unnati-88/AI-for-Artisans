from fastapi import APIRouter

router = APIRouter()


@router.get("/timeline")
async def get_timeline():
    """Production advisor timeline — mock JSON matching ProductionAdvisor.jsx."""
    return [
        {
            "time_label": "TODAY",
            "title": "Indigo Dyeing Phase",
            "badge": {"label": "Safe for Dyeing", "variant": "green"},
            "description": (
                "Humidity is currently at 45% with clear skies. Perfect conditions "
                "for outdoor drying of the new indigo batch."
            ),
            "pills": [
                {"label": "☀️ Full Sun, 32°C", "variant": "outline"},
                {"label": "💧 Low Humidity", "variant": "outline"},
            ],
            "ai_advice": None,
            "image_url": None,
            "footer_link": None,
        },
        {
            "time_label": "TOMORROW",
            "title": "Silk Weaving",
            "badge": {"label": "High Priority", "variant": "amber"},
            "description": (
                "Begin weaving the red and gold silk sarees. AI predicts a 20% "
                "surge in demand in the next 3 weeks."
            ),
            "pills": None,
            "ai_advice": "Keep silk yarns away from direct afternoon heat.",
            "image_url": None,
            "footer_link": None,
        },
        {
            "time_label": "IN 3 WEEKS",
            "title": "Diwali Festival Readiness",
            "badge": None,
            "description": (
                "All festive stock should be ready for dispatch to major mandis. "
                "Target completion for all red/gold patterns."
            ),
            "pills": [
                {"label": "Target: 50 Sarees", "variant": "solidAmber"},
                {"label": "Current: 12 Ready", "variant": "solidGreen"},
            ],
            "ai_advice": None,
            "image_url": "/images/diwali_sarees.jpg",
            "footer_link": None,
        },
        {
            "time_label": "NEXT MONTH",
            "title": "Design Planning: Wedding Season",
            "badge": {"label": "Planning", "variant": "pink"},
            "description": (
                "Start drafting new peacock and floral motifs. Review AI market "
                "trends for trending color palettes in urban markets."
            ),
            "pills": None,
            "ai_advice": None,
            "image_url": None,
            "footer_link": {"label": "View Trend Report", "href": "/trends"},
        },
    ]
