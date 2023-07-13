"""SQLAlchemy Session

    See: https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@contextmanager
def Session():
    engine = create_engine(
        url="postgresql+psycopg2://USERNAME:PASSWD@DBHOST:DBPORT/DBNAME",  # changeme
        echo=True,
    )
    try:
        session = sessionmaker(bind=engine, autocommit=True, autoflush=True)
        with session() as sess:
            with sess.begin():
                yield sess
    finally:
        engine.dispose()
