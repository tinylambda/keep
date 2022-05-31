import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Felix", age=36)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_graphql:app --reload
# Access http://127.0.0.1:8000/graphql
