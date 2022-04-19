from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session, Mapper, Query
from sqlalchemy.orm.scoping import scoped_session
from db.schemas import start_mappers
from typing import ContextManager


@contextmanager
def new_session(**kwargs) -> ContextManager[Session]:
    new_session = session_factory(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except:
        new_session.rollback()
        raise
    finally:
        new_session.close()


def _get_query_cls(mapper, session):
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)

start_mappers()


session_factory = sessionmaker(query_cls=_get_query_cls)
session: scoped_session = scoped_session(session_factory)

