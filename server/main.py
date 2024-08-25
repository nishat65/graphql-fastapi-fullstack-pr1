import os
from fastapi import FastAPI
from dotenv import load_dotenv
from gql.index import gql_router
from routers.users_router import UsersController

load_dotenv()

app = FastAPI()
api = FastAPI()


@app.get("/")
def root():
    return {"message": "OK"}


api.include_router(UsersController().router, prefix="/users", tags=["users"])
api.include_router(gql_router, prefix="/gql", tags=["graphql"])
app.mount("/api", api)
