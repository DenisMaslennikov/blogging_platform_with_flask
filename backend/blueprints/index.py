from datetime import datetime
from math import ceil

from flask import Blueprint, render_template, current_app, request
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from backend.models import Post

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    """Главная страница"""
    per_page = current_app.config.get('PAGINATED_BY', 10)
    page = request.args.get('page', 1)
    # posts = db.paginate(Post.query.order_by(desc(Post.pub_date)).options(
    #     joinedload(Post.author),
    #     joinedload(Post.category),
    #     joinedload(Post.tags),
    #     joinedload(Post.comments),
    # ), per_page=per_page, page=page)

    posts = Post.query.options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags),
        joinedload(Post.comments),
    ).order_by(desc(Post.pub_date)).filter(
        Post.pub_date <= datetime.now(), Post.published
    ).limit(
        per_page * page
    ).offset(
        per_page * (page - 1)
    ).all()
    page_count = ceil(len(posts) / per_page)

    return render_template(
        'main.html',
        posts=posts,
        page_count=page_count,
        title='Платформа для блогинга',
    )