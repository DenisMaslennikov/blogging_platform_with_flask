from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import BaseModel


class Blog(BaseModel):
    """Модель блога"""
    __tablename__ = 'blogs'

    url = Column(String(100), nullable=False, unique=True, doc='Адрес блога')
    title = Column(String(100), nullable=False, doc='Заголовок')
    description = Column(String(500), nullable=False, doc='Описание')
    user_id = Column(Integer, ForeignKey('users.id'), doc='Пользователь')

    user = relationship('User', back_populates='blog')
