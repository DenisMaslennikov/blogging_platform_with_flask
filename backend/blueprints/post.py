from flask import Blueprint, render_template
from sqlalchemy.orm import joinedload

from backend.models import Post

post_blueprint = Blueprint('post', __name__)

@post_blueprint.route('/<slug>')
def post_detail(slug):
    """Просмотр конкретного поста"""
    post = Post.query.options(
        joinedload(Post.comments),
        joinedload(Post.author),
        joinedload(Post.tags),
    ).filter(Post.slug == slug).first()

    return render_template('detail.html', post=post)