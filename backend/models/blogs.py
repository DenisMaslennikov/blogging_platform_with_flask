import re

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, validates

from .base_model import BaseModel


class Blog(BaseModel):
    """Модель блога"""
    __tablename__ = 'blogs'

    url = Column(String(100), nullable=False, unique=True, doc='Адрес блога')
    title = Column(String(100), nullable=False, doc='Заголовок')
    description = Column(String(500), nullable=True, doc='Описание')
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
        doc='Пользователь',
    )

    user = relationship('User', back_populates='blog', uselist=False)
    posts = relationship('Post', back_populates='blog', uselist=True)

    def __repr__(self):
        return self.title

    @validates('url')
    def validate_url(self, key, value):
        """Проверка поля url на допустимые символы"""
        assert re.match(r'^[a-z0-9](?:[a-z0-9_-]*[a-z0-9])?$', value), (
            'Некорректное значение поля url оно может содержать только цифры, '
            'буквы латинского алфавита и символы "-_"'
        )
        return value
