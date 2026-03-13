from fastapi import APIRouter, Depends
from app.common.schemas.user import UserLogin, AuthResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.common.models.user import User
from app.common.services.login_service import login_user_service

router = APIRouter(prefix="/driver/auth", tags=["Driver Authentication"])

@router.post("/login",response_model=AuthResponse)
async def driver_login(credentials: UserLogin, db: Session = Depends(get_db)):
    result = login_user_service(credentials, db)
    return {
        "access_token": result["access_token"],
        "refresh_token": result["refresh_token"],
        "token_type": "bearer",
        "user_type": "driver"
    }