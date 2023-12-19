from sqlalchemy import Column, Integer, ForeignKey

from .base_model import BaseModel

class TagsPostsAssociation(BaseModel):
    """Модель для связи моделей тегов и постов"""
    __tablename__ = 'tags_posts'

    tag_id = Column(Integer, ForeignKey('tags.id'), doc='Теги')
    post_id = Column(Integer, ForeignKey('posts.id'),doc='Пост')
