from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import BaseModel


class Comment(BaseModel):
    """Модель комментария к посту"""
    __tablename__ = 'comments'

    text = Column(String, nullable=False, doc='Текст комментария')
    post_id = Column(
        Integer,
        ForeignKey('posts.id'),
        nullable=False,
        doc='Пост',
    )
    author_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
        doc='Автор',
    )

    author = relationship('User', back_populates='comments', uselist=False)
    post = relationship('Post', back_populates='comments', uselist=False)
