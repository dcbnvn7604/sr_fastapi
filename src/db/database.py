from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from db._database import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def transaction(fn):
    def _fn(*args, **kwargs):
        if args[0].db.in_transaction():
            return fn(*args, **kwargs)
               
        with args[0].db.begin():
            return fn(*args, **kwargs)

    return _fn
