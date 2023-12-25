from datetime import datetime

from flask import send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import func, column
from sqlalchemy.orm import joinedload

from backend.core.app import get_app
from backend.core.config import DebugConfig
from backend.core.db import db
from backend.models import Category, Post

app = get_app(DebugConfig)

toolbar = DebugToolbarExtension(app)

db.init_app(app)

@app.context_processor
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


    return dict(categories=categories)

@app.route('/uploads/<name>')
def download_file(name: str):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        use_reloader=True,
        passthrough_errors=True,
        debug=True
    )
