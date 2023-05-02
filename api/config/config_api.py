from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
# from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

from .config_db import SessionLocal

app = FastAPI()

# app.add_middleware(
#     HTTPSRedirectMiddleware,
# )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
