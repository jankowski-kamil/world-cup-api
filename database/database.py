from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/worldcup")
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()
