from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ml", tags=["ML"])


class DescriptionRequest(BaseModel):
    keywords: str = ""


class DescriptionResponse(BaseModel):
    en: str
    hi: str


@router.post("/generate-description", response_model=DescriptionResponse)
async def generate_description(data: DescriptionRequest):
    """Mock NLP bilingual description generator — per Blueprint §3."""
    keywords = data.keywords.strip() if data.keywords else "handcrafted artisan product"
    return DescriptionResponse(
        en=(
            f"Exquisite hand-woven scarf crafted from pure mulberry silk. "
            f"Featuring a vibrant {keywords} pattern, this piece embodies "
            f"traditional craftsmanship with a modern touch. Perfect for "
            f"discerning buyers seeking authentic Indian artisanal products."
        ),
        hi=(
            f"शुद्ध शहतूत रेशम से तैयार किया गया उत्तम हाथ से बुना हुआ दुपट्टा। "
            f"एक जीवंत {keywords} पैटर्न की विशेषता, यह टुकड़ा आधुनिक स्पर्श के साथ "
            f"पारंपरिक शिल्प कौशल का प्रतीक है।"
        ),
    )
