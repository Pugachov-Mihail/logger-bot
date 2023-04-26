FROM tiangolo/uvicorn-gunicorn:python3.9-slim

WORKDIR /api

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2  \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "main.py"]
