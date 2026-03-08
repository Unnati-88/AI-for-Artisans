from fastapi import APIRouter, Query

router = APIRouter()


@router.get("")
async def get_trends(tab: str = Query("All Trends", description="Filter tab")):
    """Get trend feed data — mock JSON matching Trends.jsx."""
    all_trends = [
        {
            "id": 1,
            "author_name": "Meera Textile Insights",
            "author_initial": "M",
            "category": "Wedding Season",
            "posted_ago": "2 hours ago",
            "image_url": "/images/loom_weaving.png",
            "body_text": (
                "Traditional Banarasi handlooms with festive reds, deep golds, and royal "
                "blues are seeing peak demand this wedding season. Weavers report a 40% surge "
                "in orders — lotus and peacock motifs in magenta-gold are the top request."
            ),
            "tags": ["#WeddingSilk", "#FloralMotif"],
            "likes": "1.2k",
            "comments": 89,
        },
        {
            "id": 2,
            "author_name": "Arjun Dye Works",
            "author_initial": "A",
            "category": "Sustainable Dyes",
            "posted_ago": "5 hours ago",
            "image_url": "/images/natural_dyes.png",
            "body_text": (
                "Eco-conscious global buyers are actively sourcing naturally dyed cotton — "
                "indigo, turmeric, and madder red are the top picks. Market demand is up 25% "
                "this quarter, with premium pricing for certified natural dye products."
            ),
            "tags": ["#NaturalDyes", "#IndigoRevival", "#SustainableCraft"],
            "likes": "856",
            "comments": 42,
        },
        {
            "id": 3,
            "author_name": "Rajasthan Craft Hub",
            "author_initial": "R",
            "category": "Cotton",
            "posted_ago": "1 day ago",
            "image_url": "/images/block_print.png",
            "body_text": (
                "Sanganeri and Bagru block-printed kurtas and dupattas are surging in export "
                "orders — the US and EU markets alone have seen a 35% increase in demand for "
                "authentic hand-block prints this season."
            ),
            "tags": ["#BlockPrint", "#SanganeriPrint", "#RajasthanCraft"],
            "likes": "2.1k",
            "comments": 156,
        },
    ]

    if tab == "All Trends":
        return all_trends
    return [t for t in all_trends if t["category"] == tab]


@router.get("/intelligence")
async def get_intelligence():
    """AI suggestion + raw material forecast sidebar data."""
    return {
        "ai_suggestion": {
            "title": "Artisan AI Suggestion",
            "subtitle": "Based on your browsing history",
            "text": (
                "The magenta lotus design shown in the feed has a 20% higher profit "
                "margin if produced using the locally sourced raw silk currently on sale."
            ),
            "action": "Calculate Potential Profit",
        },
        "material_forecast": [
            {"name": "Mulberry Silk", "price": "₹4,200", "status": "Low Stock Alert", "trend": "+8.3% ↗"},
            {"name": "Cotton Yarn", "price": "₹850", "status": "Stable Demand", "trend": "+1.1% ↗"},
            {"name": "Natural Indigo", "price": "₹1,800", "status": "Price Drop", "trend": "-3.4% ↘"},
        ],
    }
