from sqlalchemy.engine.create import create_engine
from api.domain.dtos import Gender, Citizen
from sqlalchemy.sql.schema import MetaData, PrimaryKeyConstraint
from sqlalchemy.orm import mapper
from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey,
    Date, Enum, ForeignKeyConstraint
)
from config.pg import DEFAULT_PG_URL


engine = create_engine(DEFAULT_PG_URL)
metadata = MetaData(bind=engine)


# import_table = Table(
#     "import", metadata,
#     Column("import_id", Integer, primary_key=True),
# )


citizen_table = Table(
    "citizen", metadata,
    # Column("import_id", Integer, ForeignKey("import.import_id")),
    Column("citizen_id", Integer, primary_key=True, autoincrement=True),
    Column("town", String(255), nullable=False),
    Column("building", String(255), nullable=False),
    Column("apartment", Integer, nullable=False),
    Column('name', String(255), nullable=False),
    Column("birth_date", Date, nullable=False),
    Column("gender", Enum(Gender, name="gender"), nullable=False),
)


# relation_table = Table(
#     "relation", metadata,
#     Column('import_id', Integer, primary_key=True),
#     Column('citizen_id', Integer, primary_key=True),
#     Column('relative_id', Integer, primary_key=True),
#     ForeignKeyConstraint(
#         ('import_id', 'citizen_id'),
#         ('citizen.import_id', 'citizen.citizen_id')
#     ),
#     ForeignKeyConstraint(
#         ('import_id', 'relative_id'),
#         ('citizen.import_id', 'citizen.citizen_id')
#     ),
# )


def start_mappers():
    mapper(Citizen, citizen_table)

