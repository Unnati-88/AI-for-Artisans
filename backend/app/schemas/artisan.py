from pydantic import BaseModel


class ArtisanRead(BaseModel):
    id: int
    name: str
    mobile: str
    role: str
    location: str
    member_since: str
    bio: str
    skills: list[str]
    avatar_url: str
    lifetime_earnings: str
    completed_orders: int
    fulfillment_pct: int
    market_accuracy: int
    workshops: int
    awards: int
    countries: int

    class Config:
        from_attributes = True


class ArtisanUpdate(BaseModel):
    name: str | None = None
    role: str | None = None
    location: str | None = None
    bio: str | None = None
    skills: list[str] | None = None
    avatar_url: str | None = None
