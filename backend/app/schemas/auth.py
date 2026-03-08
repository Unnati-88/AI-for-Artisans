from pydantic import BaseModel


class LoginRequest(BaseModel):
    mobile: str
    password: str


class SignupRequest(BaseModel):
    name: str
    mobile: str
    password: str
    role: str = "Artisan"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
