from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel
from .tags_posts import TagsPostsAssociation


class Tag(BaseModel):
    """Модель тегов к постам"""
    __tablename__ = 'tags'

    name = Column(String(100), unique=True, doc='Тег')
    slug = Column(String(100), unique=True, doc='Слаг')

    posts = relationship(
        'Post',
        secondary=TagsPostsAssociation.__table__,
        back_populates='tags',
        uselist=True,
    )
