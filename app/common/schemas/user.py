from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional
from datetime import datetime
from app.common.models.user import RoleType

# ---------------------------
# Base User Schema
# ---------------------------

class UserBase(BaseModel):
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


# ---------------------------
# User Registration
# ---------------------------

class UserCreate(BaseModel):
    full_name: str
    phone: str
    password: str
    role: RoleType   # required


# ---------------------------
# Login with Phone
# ---------------------------

class UserLogin(BaseModel):
    phone: str
    password: str


# ---------------------------
# Google Login
# ---------------------------

class GoogleLogin(BaseModel):
    id_token: str


# ---------------------------
# Update User
# ---------------------------

class UserUpdate(BaseModel):
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


# ---------------------------
# User Response
# ---------------------------

class UserOut(BaseModel):
    id: int
    phone: Optional[str]
    email: Optional[str]

    is_active: bool
    is_verified: bool

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ---------------------------
# Auth Token Response
# ---------------------------

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------------------------
# Token Payload
# ---------------------------

class TokenPayload(BaseModel):
    user_id: int
    exp: Optional[int] = None


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user_type: str