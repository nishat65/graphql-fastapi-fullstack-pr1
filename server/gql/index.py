# from strawberry.tools import merge_types
from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from gql.gql import schema

gql_router = GraphQLRouter(schema=schema)
