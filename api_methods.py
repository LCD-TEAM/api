from fastapi import FastAPI
from models.article import Article
from models.news import News
import temp_news

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

@app.get('/roles/')
async def get_roles():
    return temp_news.roles

@app.get('/spheres/')
async def get_spheres(role: str):
    return temp_news.get_spheres(role)

@app.get('/news/')
async def get_news(role: str, sphere: str):
    return temp_news.get_news(role, sphere)
