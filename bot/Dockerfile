FROM python:3.10-slim

WORKDIR /bot

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc vim\
    && pip install psycopg2  \
    && pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "main.py"]

