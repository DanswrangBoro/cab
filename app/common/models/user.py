from sqlalchemy import Column, Integer, String, Boolean, DateTime, CheckConstraint, Enum, ForeignKey, UniqueConstraint
import enum
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=True)

    password = Column(String(255), nullable=False)
    google_id = Column(String(255), unique=True, nullable=True)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    roles = relationship("UserRole", back_populates="user")

    __table_args__ = (
        CheckConstraint(
            "(phone IS NOT NULL) OR (email IS NOT NULL)",
            name="phone_or_email_required"
        ),
    )

class RoleType(str, enum.Enum):
    rider = "rider"
    driver = "driver"

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    role = Column(Enum(RoleType), nullable=False)

    user = relationship("User", back_populates="roles")

    __table_args__ = (
        UniqueConstraint("user_id", "role", name="unique_user_role"),
    )