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
    UPLOAD_FOLDER = '/media/'


class DebugConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
