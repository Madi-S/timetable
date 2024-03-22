import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name='John Doe', age=31)


schema = strawberry.Schema(query=Query)

route = GraphQL(schema)
