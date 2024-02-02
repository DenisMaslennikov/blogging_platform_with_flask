import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR.parent.joinpath('config', '.env'))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:'
        f'{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DB_HOST")}'
        f':{os.getenv("DB_PORT")}/{os.getenv("POSTGRES_DB")}'
    )
    ROOT_PATH = BASE_DIR
    UPLOAD_FOLDER = BASE_DIR / 'media'
    UPLOAD_URL_PREFIX = '/media/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    PAGINATED_BY = 10


class DebugConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PANELS = ('flask_debugtoolbar_sqlalchemy.SQLAlchemyPanel', )


class ProductionConfig(BaseConfig):
    DEBUG = False
