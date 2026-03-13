from fastapi import APIRouter, Depends
from app.common.schemas.user import UserCreate
from app.common.models.user import RoleType
from app.database import get_db
from sqlalchemy.orm import Session
from app.common.services.registration_service import register_user_service

router = APIRouter(prefix="/rider/auth", tags=["Rider Registration"])

@router.post("/register")
async def rider_register(
    full_name: str,
    phone: str,
    password: str,
    db: Session = Depends(get_db)
):
    user_data = UserCreate(
        full_name=full_name,
        phone=phone,
        password=password,
        role=RoleType.rider
    )
    
    new_user = register_user_service(user_data, db)
    
    return {
        "message": "Rider registered successfully",
        "user_id": new_user.id
    }
