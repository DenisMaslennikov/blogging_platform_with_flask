from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel
from .tags_posts import TagsPostsAssociation


class Tag(BaseModel):
    """Модель тегов к постам"""
    __tablename__ = 'tags'

    name = Column(String(100), unique=True, doc='Тег', nullable=False)
    slug = Column(String(100), unique=True, doc='Слаг', nullable=False)

    posts = relationship(
        'Post',
        secondary=TagsPostsAssociation.__table__,
        back_populates='tags',
        uselist=True,
    )

    def __repr__(self):
        return self.name
