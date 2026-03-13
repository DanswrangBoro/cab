from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.common.models.user import User
from app.common.schemas.user import UserLogin
from app.core.security import verify_password, create_access_token, create_refresh_token 


def login_user_service(credentials: UserLogin, db: Session):
    # login using phone
    user = db.query(User).filter(User.phone == credentials.phone).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token({"user_id": user.id})
    refresh_token = create_refresh_token({"user_id": user.id})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user
    }