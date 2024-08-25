import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from db.conn import get_db

from db.user_model import User


@strawberry.type
class UserReadSchemaGql:
    id: str
    username: str = strawberry.field(description="User name", name="username")
    email: str = strawberry.field(description="User email", name="email")
    password: str = strawberry.field(description="User password", name="password")
    created_at: str


@strawberry.input
class UserCreateSchemaGql:
    username: str = strawberry.field(description="User name", name="username")
    email: str = strawberry.field(description="User email", name="email")
    password: str = strawberry.field(description="User password", name="password")


@strawberry.input
class UserUpdateSchemaGql:
    username: Optional[str] = strawberry.field(description="User name", name="username")
    email: Optional[str] = strawberry.field(description="User email", name="email")
    password: Optional[str] = strawberry.field(
        description="User password", name="password"
    )


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[UserReadSchemaGql]:
        db: Session = next(get_db())
        users = db.query(User).all()
        return [
            UserReadSchemaGql(
                id=user.id,
                username=user.username,
                email=user.email,
                password=user.password,
                created_at=str(user.created_at),
            )
            for user in users
        ]

    @strawberry.field
    def user(self, id: int) -> UserReadSchemaGql | None:
        db: Session = next(get_db())
        user = db.query(User).filter(User.id == id).first()
        if not user:
            return None
        return UserReadSchemaGql(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            created_at=str(user.created_at),
        )


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_users(self, user: UserCreateSchemaGql) -> UserReadSchemaGql:
        db: Session = next(get_db())
        user = User(username=user.username, email=user.email, password=user.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserReadSchemaGql(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            created_at=str(user.created_at),
        )

    @strawberry.mutation
    def delete_user(self, id: int) -> UserReadSchemaGql | None:
        db: Session = next(get_db())
        user = db.query(User).filter(User.id == id).first()
        if not user:
            return None
        db.delete(user)
        db.commit()
        return UserReadSchemaGql(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            created_at=str(user.created_at),
        )

    @strawberry.mutation
    def update_user(
        self, id: int, new_user: UserUpdateSchemaGql
    ) -> UserReadSchemaGql | None:
        db: Session = next(get_db())
        user = db.query(User).filter(User.id == id).first()
        if not user:
            return None
        if new_user.username:
            user.username = new_user.username
        if new_user.email:
            user.email = new_user.email
        if new_user.password:
            user.password = new_user.password
        db.commit()
        db.refresh(user)
        return UserReadSchemaGql(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            created_at=str(user.created_at),
        )


schema = strawberry.Schema(Query, mutation=Mutation)
