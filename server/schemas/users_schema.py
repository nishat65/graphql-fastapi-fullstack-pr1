from datetime import datetime
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    username: str = Field(
        default=None,
        description="User name",
        # alias="username",
        max_length=250,
        min_length=2,
    )
    email: str = Field(
        default=None, description="User email", max_length=250, min_length=2
    )
    password: str = Field(
        default=None, description="User password", max_length=250, min_length=6
    )

    class Config:
        from_attributes = True


class UserReadSchema(UserBaseSchema):
    id: str
    created_at: str

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema):
    pass
