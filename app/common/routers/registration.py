from fastapi import APIRouter, Depends, HTTPException, status
from app.common.schemas.user import UserCreate
from app.common.models.user import User
from app.core.security import hash_password
from app.database import get_db
from sqlalchemy.orm import Session
from app.common.services.registration_service import register_user_service

router = APIRouter(prefix="/auth", tags=["Registration"])

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = register_user_service(user, db)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }