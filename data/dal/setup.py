from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import get_settings

s = get_settings()


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{s.pg_username}:{s.pg_password}" \
                          f"@{s.pg_host}:{s.pg_port}/{s.pg_database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
