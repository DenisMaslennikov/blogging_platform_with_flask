from datetime import datetime
from math import ceil

from flask import Blueprint, render_template, current_app, request
from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from backend.models import Post

month_blueprint = Blueprint('month', __name__)

@month_blueprint.route('/<month>/<year>')
def by_month(month, year):
    """Просмотр страницы тега"""
    per_page = current_app.config.get('PAGINATED_BY', 10)
    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(desc(Post.pub_date)).options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags),
        joinedload(Post.comments),
    ).filter(
        func.extract('month', Post.pub_date) == month,
        func.extract('year', Post.pub_date) == year,
    ).filter(
        Post.published,
        Post.pub_date <= datetime.now()
    ).paginate(page=page, per_page=per_page)
    return render_template(
        'main.html',
        posts=posts,
        title=f'Платформа для блогинга просмотр постов за {month}/{year}',
    )
