from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.common.models.user import UserRole
from app.common.models.user import User
from app.common.schemas.user import UserCreate
from app.core.security import hash_password


def register_user_service(user: UserCreate, db: Session):

    # check phone duplicate
    existing_phone = db.query(User).filter(User.phone == user.phone).first()
    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this phone number already exists"
        )

    # create user
    new_user = User(
        full_name=user.full_name,
        phone=user.phone,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # create role
    user_role = UserRole(
        user_id=new_user.id,
        role=user.role
    )

    db.add(user_role)
    db.commit()

    return new_user