from sqlalchemy import TEXT, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel
from .tags_posts import TagsPostsAssociation


class Post(BaseModel):
    """Модель поста в блоге"""
    __tablename__ = 'posts'

    title = Column(String(100), nullable=False, doc='Заголовок')
    text = Column(TEXT, nullable=False, doc='Текст поста')
    slug = Column(String(100), nullable=False, doc='Слаг')
    author_id = Column(Integer, ForeignKey('users.id'), doc='Автор')
    blog_id = Column(Integer, ForeignKey('blogs.id'), doc='Блог')
    pub_date = Column(DateTime, doc='Дата публикации')
    post_image_file = Column(
        String(255), nullable=True, doc='Изображение к посту'
    )
    anons = Column(String(500), nullable=False, doc='Анонс')
    views = Column(Integer, default=0, nullable=False, doc='Просмотров')
    category_id = Column(Integer, ForeignKey('categories.id'), doc='Категория')

    author = relationship('User', back_populates='posts', uselist=False)
    blog = relationship('Blog', back_populates='posts', uselist=False)
    comments = relationship(
        'Comment',
        back_populates='post',
        uselist=True,
        order_by = 'Comment.created_utc',
    )
    tags = relationship(
        'Tag',
        secondary=TagsPostsAssociation.__table__,
        back_populates='posts',
        uselist=True
    )
    category = relationship('Category', back_populates='posts', uselist=False)

    def __repr__(self):
        return self.title
