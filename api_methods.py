from fastapi import FastAPI

app = FastAPI()

roles = ['Бухгалтер', 'Ген. директор']

spheres = [
    {'role': 'Бухгалтер', 'spheres': ['Финансы', 'Учет', 'Законы']},
    {'role': 'Ген. директор', 'spheres': ['Бизнес', 'Технологии', 'Управление']}
    ]

@app.get('/')
async def root():
    return "test"

@app.get('/roles/')
async def get_roles():
    return roles

@app.get('/spheres/')
async def get_spheres(role: str):
    return next(sphere['spheres'] for sphere in spheres if sphere['role'] == role)

@app.get('/news/')
async def get_news(role: str, sphere: str):
    if sphere == 'Бизнес':
        return {
            'title': 'заголовок новости',
            'content': 'бизнес-новость'
        }
    else:
        return {
            'title': 'заголовок новости',
            'content': 'другая новость'
        }