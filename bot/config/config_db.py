from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "sqlite:///test.db"

# connect_args={"check_same_thread": False} only sqlite
engine = create_engine(DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(atr):
    db: Session = SessionLocal()
    try:
        db.add(atr)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
