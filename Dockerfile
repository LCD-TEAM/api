FROM python:3.9-alpine

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

ENTRYPOINT [ "python", "main.py" ]