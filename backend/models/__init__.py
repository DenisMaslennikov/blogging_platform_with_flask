from flask_sqlalchemy import SQLAlchemy

from .base_model import BaseModel
from .blogs import Blog
from .comments import Comment
from .posts import Post
from .tags import Tag
from .tags_posts import TagsPostsAssociation
from .users import User

__all__ = (
    'TagsPostsAssociation',
    'Tag',
    'Post',
    'User',
    'Comment',
    'Blog',
    'BaseModel',
)

db = SQLAlchemy()
