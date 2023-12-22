from flask import Flask

from backend.blueprints import blueprints


def get_app(config) -> Flask:
    app = Flask(
        __name__,
        static_folder=config.ROOT_PATH / 'static',
        template_folder=config.ROOT_PATH / 'templates'
    )
    app.config.from_object(config)

    # db.init_app(app)

    for blueprint in blueprints:
        app.register_blueprint(
            blueprint.blueprint, url_prefix=blueprint.url_prefix
        )

    return app
