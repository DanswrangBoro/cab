from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.common.schemas.user import UserLogin
from app.database import get_db
from sqlalchemy.orm import Session
from app.common.models.user import User
from app.common.services.login_service import login_user_service

router = APIRouter(prefix="/rider/auth", tags=["Rider Authentication"])


@router.post("/login")
async def rider_login(credentials: UserLogin, db: Session = Depends(get_db)):

    result = login_user_service(credentials, db)
    return {
        "access_token": result["access_token"],
        "refresh_token": result["refresh_token"],
        "token_type": "bearer",
        "user_type": "rider"
    }