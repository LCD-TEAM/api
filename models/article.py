from datetime import date

class Article():
    date_published: date
    title: str
    content: str
    tags: list[str]

    def __init__(self, date_published: date, title: str, content: str, tags: list[str]):
        self.date_published = date_published
        self.title = title
        self.content = content
        self.tags = tags