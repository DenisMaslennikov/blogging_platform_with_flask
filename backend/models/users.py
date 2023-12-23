from sqlalchemy import Column, String, Boolean
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
    is_active = Column(
        Boolean, nullable=False, default=False, doc='Пользователь активен'
    )
    about = Column(String(300), nullable=True, doc='О себе')
    user_image = Column(
        String(255), nullable=True, doc='Изображение пользователя'
    )

    blog = relationship('Blog', back_populates='user', uselist=False)
    posts = relationship('Post', back_populates='author', uselist=True)
    comments = relationship(
        'Comment',
        back_populates='author',
        uselist=True,
        order_by='desc(Comment.created_utc)',
    )

    def  __repr__(self):
        return self.username
