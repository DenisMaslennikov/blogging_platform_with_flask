from flask import send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from core.app import get_app
from core.config import DebugConfig
from backend.core.db import db
from backend.models import Category

app = get_app(DebugConfig)

toolbar = DebugToolbarExtension(app)

db.init_app(app)

@app.context_processor
def push_base_context():
    """Базовый контекст для всех страниц"""
    categories = Category.query.options(
        joinedload(Category.posts)
    ).group_by(Category.slug, Category.name, Category.id).add_column(
        func.count(Category.posts).label('post_count')).all()
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
