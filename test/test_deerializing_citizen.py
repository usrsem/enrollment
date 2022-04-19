from marshmallow.exceptions import ValidationError
import pytest
from api.domain.dtos import Citizen, Gender
from api.domain.marshmallow_schemas import CitizenSchema
from copy import copy
from datetime import datetime


citizen_as_dict: dict[str, str] = {
    "citizen_id": "0",
    "town": "some_town",
    "building": "some_building",
    "apartment": "7",
    "name": "some_name",
    "birth_date": "18.04.2002",
    "gender": "male"
}

original_citizen: Citizen = Citizen(
    citizen_id=0,
    town="some_town",
    building="some_building",
    apartment=7,
    name="some_name",
    birth_date=datetime.strptime("18.04.2002", "%d.%m.%Y").date(),
    gender=Gender.MALE
)


def test_citizen_deserialization() -> None:
    schema: CitizenSchema = CitizenSchema()
    after = schema.load(citizen_as_dict)
    msg: str = f"{citizen_as_dict=}\n{after=}\n{original_citizen=}"
    assert after == original_citizen, msg


def test_wrang_apartment_type() -> None:
    before: dict[str, str] = copy(citizen_as_dict)
    schema: CitizenSchema = CitizenSchema()
    before["apartment"] = "asdf"
    with pytest.raises(ValidationError):
        schema.load(before)

