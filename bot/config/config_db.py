import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.ext.declarative import declarative_base

logging.basicConfig(level=logging.INFO)

DATABASE = "sqlite:///test.db"

# connect_args={"check_same_thread": False} only sqlite
engine = create_engine(DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = scoped_session(SessionLocal)

Base = declarative_base()


def get_db(atr=None):
    db = session
    try:
        db.add(atr)
        db.commit()
        db.refresh(atr)
    except:
        db.rollback()
    finally:
        db.close()
        return atr

