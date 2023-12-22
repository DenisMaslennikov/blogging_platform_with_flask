from flask import Blueprint, render_template, current_app, request
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from backend.core.db import db
from backend.models import Post, Category

category_blueprint = Blueprint('category', __name__)

@category_blueprint.route('/<slug>')
def by_category(slug):
    """Просмотр страницы тега"""
    per_page = current_app.config.get('PAGINATED_BY', 10)
    page = request.args.get('page', 1)
    posts = db.paginate(Post.query.order_by(desc(Post.pub_date)).options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags),
        joinedload(Post.comments),
    ).filter(
        Post.category.has(Category.slug == slug)), per_page=per_page, page=page
    )
    return render_template('index.html', posts=posts)