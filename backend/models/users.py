from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel


class User(BaseModel):
    """Модель пользователя"""
    __tablename__ = 'users'

    username = Column(
        String(100), nullable=False, doc='Имя пользователя', unique=True
    )
    email = Column(String(100), nullable=False, doc='Е-мейл', unique=True)
    password = Column(String(300), nullable=False, doc='Хеш пароля')
    first_name = Column(String(100), nullable=True, doc='Имя')
    last_name = Column(String(100), nullable=True, doc='Фамилия')
    middle_name = Column(String(100), nullable=True, doc='Отчество')

    blog = relationship('Blog', back_populates='user', uselist=False)
    posts = relationship('Post', back_populates='author', uselist=True)
