from datetime import datetime

from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload

from backend.core import constants
from backend.models import Post, Category, Tag


def push_base_context():
    """Базовый контекст для всех страниц"""
    categories = Category.query.join(
        Post, Category.id == Post.category_id
    ).group_by(
        Category.slug, Category.name, Category.id
    ).filter(Post.pub_date < datetime.now(), Post.published).with_entities(
        Category.slug,
        Category.name,
        func.count(Category.posts).label('post_count')
    )

    archives = Post.query.group_by(
        func.extract('month', Post.pub_date),
        func.extract('year', Post.pub_date),
    ).filter(Post.pub_date <= datetime.now(), Post.published).with_entities(
        func.extract('month', Post.pub_date).label('month'),
        func.extract('year', Post.pub_date).label('year'),
        func.count(Post.id).label('post_count'),
    ).order_by(
        desc(func.extract('year', Post.pub_date)),
        desc(func.extract('month', Post.pub_date)),
    ).all()

    popular = Post.query.order_by(desc(Post.views)).options(
        joinedload(Post.author)
    ).filter(
        Post.published,
        Post.pub_date <= datetime.now(),
    ).limit(constants.POSTS_IN_POPULAR)

    tag_cloud = Tag.query.join(Tag.posts).order_by(
        desc(func.count(Post.id))
    ).group_by(Tag.name, Tag.slug, Tag.id).filter(
        Post.published, Post.pub_date <= datetime.now()
    ).limit(
        constants.TAGS_IN_TAG_CLOUD
    )

    return dict(
        categories=categories,
        archives=archives,
        popular=popular,
        tag_cloud=tag_cloud
    )
