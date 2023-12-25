from datetime import datetime

from flask import Blueprint, render_template
from sqlalchemy.orm import joinedload

from backend.core.db import db
from backend.models import Post

post_blueprint = Blueprint('post', __name__)

@post_blueprint.route('/<slug>')
def post_detail(slug):
    """Просмотр конкретного поста"""
    post = Post.query.options(
        joinedload(Post.comments),
        joinedload(Post.author),
        joinedload(Post.tags),
    ).filter(Post.slug == slug).filter(
        Post.pub_date <= datetime.now(), Post.published
    ).first()
    post.views += 1
    db.session.commit()

    return render_template('detail.html', post=post)