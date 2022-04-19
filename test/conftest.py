import pytest
from api.domain.dtos import Gender, Citizen
from datetime import date


@pytest.fixture
def citizen():
    return Citizen(
        1, "town1", "building1", 1, "name1", date.today(), Gender.MALE
    )

