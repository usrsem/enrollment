import pytest
from api.domain.dtos import Citizen
from api.repository.impl.SyncCitizenRepository import SyncCitizenRepository
from api.repository.AbstractCitizenRepository import AbstractCitizenRepository
from db.context import session
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from typing import Optional


@pytest.fixture
def repository():
    yield SyncCitizenRepository(session)
    session.rollback()


def test_save_citizen(
    repository: AbstractCitizenRepository,
    citizen: Citizen
) -> None:
    repository.save(citizen)

    try:
        new_citizen = session.query(Citizen).filter_by(citizen_id=1).one()
        assert citizen == new_citizen
    except NoResultFound:
        raise AssertionError("Citizen must be saved in db")


def test_find_by_citizen_id(
    repository: AbstractCitizenRepository,
    citizen: Citizen
) -> None:
    repository.save(citizen)
    new_citizen: Optional[Citizen] = repository.find_by_citizen_id(
        citizen.citizen_id)

    assert citizen == new_citizen


def test_delete_by_citizen_id(
    repository: AbstractCitizenRepository,
    citizen: Citizen
) -> None:
    repository.save(citizen)
    repository.delete_by_citizen_id(citizen.citizen_id)

    with pytest.raises(NoResultFound):
        session.query(Citizen).one()


def test_delete_by_citizen_empty_row(
    repository: AbstractCitizenRepository,
    citizen: Citizen
) -> None:
    try:
        repository.delete_by_citizen_id(citizen.citizen_id)
    except SQLAlchemyError as e:
        raise AssertionError(e)

