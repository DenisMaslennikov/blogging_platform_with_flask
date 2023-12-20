from sqlalchemy import INTEGER, TIMESTAMP, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.expression import func


class BaseModel(DeclarativeBase):

    __abstract__ = True

    id = Column(
        INTEGER,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    created_utc = Column(
        TIMESTAMP(timezone=False),
        server_default=func.now(),
        nullable=False,
        doc='Время создания записи'
    )
    update_utc = Column(
        TIMESTAMP(timezone=False),
        onupdate=func.now(),
        nullable=True,
        doc='Время последнего изменения записи'
    )
