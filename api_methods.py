from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.article import Article
from models.news import News
import temp_news
from models import graphic
from models import recommend

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return "test"

@app.get('/valute/codes')
async def get_valute_codes():
    return graphic.get_valutes()

@app.get('/valute/')
async def get_valute_course(code: str):
    return graphic.get_course_values(code)

@app.get('/roles/')
async def get_roles():
    return temp_news.roles

@app.get('/spheres/')
async def get_spheres(role: str):
    return temp_news.get_spheres(role)

@app.get('/news/')
async def get_news(role: str):
    return recommend.recommend(role)
    
