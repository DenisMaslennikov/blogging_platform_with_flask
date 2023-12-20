from flask import Flask

from ..models import db


def get_app(config) -> Flask:
    app = Flask(
        __name__,
        static_folder=config.ROOT_PATH / 'static',
        template_folder=config.ROOT_PATH / 'templates'
    )
    app.config.from_object(config)

    db.init_app(app)

    return app
