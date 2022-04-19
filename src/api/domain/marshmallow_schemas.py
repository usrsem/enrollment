from api.domain.dtos import Citizen, Gender
from datetime import date
from marshmallow.decorators import post_load
from marshmallow.exceptions import ValidationError
from marshmallow import Schema, fields, validates
from marshmallow.validate import Length, Range
from marshmallow_enum import EnumField
from typing import Any


DATE_FORMAT: str = "%d.%m.%Y"


class CitizenSchema(Schema):
    citizen_id = fields.Int()

    town = fields.Str(required=True, validate=Length(min=1, max=100))

    building = fields.Str(required=True, validate=Length(min=1, max=100))

    apartment = fields.Int(required=True, validate=Range(min=1, max=777))

    name = fields.Str(required=True, validate=Length(min=1, max=100))

    birth_date = fields.Date(required=True, format=DATE_FORMAT)

    gender = EnumField(Gender, by_value=True, required=True)

    @validates("birth_date")
    def validate_birth_date(self, value: date) -> None:
        if value > date.today():
            raise ValidationError("Birth date must be older then today")

    @post_load
    def create_citizen_dto(self, data: dict[str, Any], **kwargs) -> Citizen:
        return Citizen(**data)


class ImportSchema(Schema):
    pass

