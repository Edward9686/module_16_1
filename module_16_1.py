from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home_page():
    return 'Главная страница'


@app.get('/user/admin')
async def admin():
    return {'Вы вошли как администор'}


@app.get('/user/{user_id}')
async def user_id():
    return {f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def admin(username: str, age: int):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
