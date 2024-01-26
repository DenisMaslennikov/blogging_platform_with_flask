from flask import Flask

from backend.blueprints import blueprints
from backend.core.db import db
from backend.core.base_service import push_base_context
from backend.core.login import login_manager


def get_app(config) -> Flask:
    """Создание Flask приложения на основе переданного конфига"""
    app = Flask(
        __name__,
        static_folder=config.ROOT_PATH / 'static',
        template_folder=config.ROOT_PATH / 'templates'
    )
    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    # Добавляем базовый контекст доступный для всех страниц
    app.context_processor(push_base_context)

    for blueprint in blueprints:
        app.register_blueprint(
            blueprint.blueprint, url_prefix=blueprint.url_prefix
        )

    return app
