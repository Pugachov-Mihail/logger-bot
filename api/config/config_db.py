import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
DB_SERVER = os.getenv("POSTGRES_SERVER")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_DB = os.getenv("POSTGRES_DB")

DATABASE = f"{DB_USER}:{DB_PASSWORD}" \
           f"@{DB_SERVER}:5432/{DB_DB}"

engine = create_engine(f"postgresql+psycopg2://{DATABASE}", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = scoped_session(SessionLocal)

Base = declarative_base()

