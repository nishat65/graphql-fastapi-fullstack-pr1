from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func
from .conn import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"
