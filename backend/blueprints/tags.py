from math import ceil

from flask import Blueprint, render_template, current_app, request
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from backend.core.db import db
from backend.models import Post, Tag

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/<slug>')
def by_tag(slug):
    """Просмотр страницы тега"""
    per_page = current_app.config.get('PAGINATED_BY', 10)
    page = request.args.get('page', 1)
    posts = Post.query.order_by(desc(Post.pub_date)).options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags),
        joinedload(Post.comments),
    ).filter(Post.tags.any(Tag.slug == slug)).limit(
        per_page * page
    ).offset(
        per_page * (page - 1)).all()
    page_count = ceil(len(posts) / per_page)

    return render_template('main.html', posts=posts, page_count=page_count)