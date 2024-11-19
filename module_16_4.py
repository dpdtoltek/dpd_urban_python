from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI()

users = []


@app.get('/')
async def get_home_page() -> dict:
    return {'message': 'Главная страница'}


class User(BaseModel):
    id: int
    username: str
    age: int


def find_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None


@app.get('/user/admin')
async def get_admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get(path='/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
],
                    age: int = Path(ge=18, le=120, description='Enter age', example='24'), user: User = Body(embed=True)
                    ) -> User:
    if len(users) != 0:
        user.id = users[-1].id + 1
    else:
        user.id = 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
],
                      age: int = Path(ge=18, le=120, description='Enter age', example='24')
                      ) -> User:
    user = find_user(user_id)
    if user is not None:
        user.username = username
        user.age = age
        return user
    else:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    user = find_user(user_id)
    if user is not None:
        users.remove(user)
        return user
    else:
        raise HTTPException(status_code=404, detail='User not found')
