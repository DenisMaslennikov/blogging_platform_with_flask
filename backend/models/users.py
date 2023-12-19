from sqlalchemy import Column, String

from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(300), nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    middle_name = Column(String(100), nullable=True)

