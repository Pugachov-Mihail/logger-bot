from fastapi import FastAPI

from .config_db import Base, engine, SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
