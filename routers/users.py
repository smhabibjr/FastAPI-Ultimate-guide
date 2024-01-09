from fastapi import APIRouter, Response, status

routers = APIRouter(
    prefix='/user',
    tags=['users']
)

@routers.get('/all')
def about():
    return f"get all users"

@routers.get('/{id}')
def about(id: int):
    return f"get user with id {id}"
