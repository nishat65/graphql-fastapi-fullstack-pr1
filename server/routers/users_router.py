from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .base_controller import BaseController
from utils.service_response import ServiceResponse
from schemas.users_schema import UserReadSchema, UserCreateSchema
from controllers.users_controller import list_all_users, create_user
from db.conn import get_db


class UsersController(BaseController):
    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route(
            path="/",
            endpoint=self.get_users,
            methods=["GET"],
            response_model=ServiceResponse[List[UserReadSchema]],
            summary="Get all users",
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.create_user,
            methods=["POST"],
            response_model=ServiceResponse[UserCreateSchema],
            summary="Create user",
        )
        super().__init__()

    @BaseController.method_logger
    def get_users(self, db: Session = Depends(get_db)):
        """
        Get all users
        """
        return list_all_users(db)

    @BaseController.method_logger
    def create_user(self, user: UserCreateSchema, db: Session = Depends(get_db)):
        """
        Create user
        """
        return create_user(user=user, db=db)
