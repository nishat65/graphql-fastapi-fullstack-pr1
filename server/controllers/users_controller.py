from typing import List
from bson.objectid import ObjectId
from sqlalchemy.orm import Session

from db.user_model import User
from utils.service_response import ServiceResponse
from schemas.users_schema import UserCreateSchema, UserReadSchema


def list_all_users(db: Session):
    result = db.query(User).all()
    return ServiceResponse[List[UserReadSchema]](result=result)


def create_user(user: UserCreateSchema, db: Session):
    db.add(User(**user.model_dump()))
    db.commit()
    return ServiceResponse[UserCreateSchema](
        result=user, status_code=201, message="Created"
    )
