from models.article import Article

class News():
    role: str
    sphere: str
    articles: list[Article]

    def __init__(self, role: str, sphere: str, articles: list[Article]):
        self.role = role
        self.sphere = sphere
        self.articles = articles