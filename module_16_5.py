from fastapi import FastAPI, Path, HTTPException, Body, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


def find_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None


@app.get('/')
async def get_users_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/admin')
async def get_admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get(path='/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': find_user(user_id)})


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
