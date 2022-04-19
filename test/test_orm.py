import pytest
from api.domain.dtos import Citizen, Gender
from datetime import date
from sqlalchemy.orm import Session
from db.context import session


def test_citizen_mapper_can_save_row():
    citizen: Citizen = Citizen(
        1, "town1", "building1", 1, "name1", date.today(), Gender.MALE
    )

    session.add(citizen)
    rows = session.query(Citizen).all()

    msg: str = f"{rows = }"
    assert rows == [citizen], msg

