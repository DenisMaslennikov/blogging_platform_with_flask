from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import BaseModel


class Post(BaseModel):
    __tablename__ = 'posts'

    title = Column(String(100), nullable=False, doc='Заголовок')
    text = Column(String, nullable=False, doc='Текст поста')
    author_id = Column(Integer, ForeignKey('users.id'), doc='Автор')
    blog_id = Column(Integer, ForeignKey('blogs.id'), doc='Блог')

    author = relationship('User', back_populates='posts', uselist=False)
    blog = relationship('Blog', back_populates='posts', uselist=False)
