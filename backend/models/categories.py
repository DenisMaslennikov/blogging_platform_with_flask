from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from  .base_model import BaseModel


class Category(BaseModel):
    """Модель категорий"""
    __tablename__ = 'categories'

    name = Column(String(100), nullable=False, doc='Название категории')
    slug = Column(String(100), nullable=False, doc='Слаг')

    posts = relationship('Post', uselist=True, back_populates='category')
