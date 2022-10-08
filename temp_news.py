from models.news import News
from models.article import Article
from datetime import date

roles = ['Бухгалтер', 'Ген. директор']

spheres = [
    {'role': 'Бухгалтер', 'spheres': ['Финансы', 'Учет']},
    {'role': 'Ген. директор', 'spheres': ['Бизнес', 'Управление']}
    ]

news = [
    News('Бухгалтер', 'Финансы', [Article(date_published=date.today(), title='заголовок1', content='контент1', tags=['тэг1', 'тэг2'])]),
    News('Бухгалтер', 'Финансы', [Article(date_published=date.today(), title='заголовок2', content='контент2', tags=['тэг1', 'тэг2'])]),
    News('Бухгалтер', 'Учет', [Article(date_published=date.today(), title='заголовок1', content='контент1', tags=['тэг1', 'тэг2'])]),
    News('Бухгалтер', 'Учет', [Article(date_published=date.today(), title='заголовок2', content='контент2', tags=['тэг1', 'тэг2'])]),
    News('Ген. директор', 'Бизнес', [Article(date_published=date.today(), title='заголовок1', content='контент1', tags=['тэг1', 'тэг2'])]),
    News('Ген. директор', 'Бизнес', [Article(date_published=date.today(), title='заголовок2', content='контент2', tags=['тэг1', 'тэг2'])]),
    News('Ген. директор', 'Управление', [Article(date_published=date.today(), title='заголовок1', content='контент1', tags=['тэг1', 'тэг2'])]),
    News('Ген. директор', 'Управление', [Article(date_published=date.today(), title='заголовок2', content='контент2', tags=['тэг1', 'тэг2'])])
    ]

def get_spheres(role: str):
    return next(sphere['spheres'] for sphere in spheres if sphere['role'] == role)

def get_news(role: str, sphere: str):
    return [n for n in news if n.role == role and n.sphere == sphere]