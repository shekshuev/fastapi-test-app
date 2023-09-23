from sqlalchemy import Column, Integer, String, DateTime
from data.dal.setup import Base
from datetime import datetime


class AccountEntity(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True, unique=True)
    role = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
