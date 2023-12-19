from sqlalchemy import Column, INTEGER, TIMESTAMP
from sqlalchemy.sql.expression import func

from . import Base


class BaseModel(Base):

    __abstract__ = True

    id = sqlalchemy.Column(
        INTEGER,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    created_utc = sqlalchemy.Column(
        TIMESTAMP(timezone=False),
        server_default=func.now(),
        nullable=False,
        doc='Время создания записи'
    )
    update_utc = sqlalchemy.Column(
        TIMESTAMP(timezone=False),
        onupdate=func.now(),
        nullable=True,
        doc='Время последнего изменения записи'
    )


