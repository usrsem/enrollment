from sqlalchemy.orm.scoping import scoped_session
from api.repository.AbstractCitizenRepository import AbstractCitizenRepository
from api.domain.dtos import Citizen
from typing import Optional
from loguru import logger as log


class SyncCitizenRepository(AbstractCitizenRepository):

    def __init__(self, session: scoped_session) -> None:
        self._session = session

    def save(self, citizen: Citizen) -> None:
        log.debug(f"Saving {citizen = }")

        self._session.add(citizen)

    def find_by_citizen_id(self, citizen_id: int) -> Optional[Citizen]:
        log.debug(f"Finding citizen with {citizen_id = }")

        return (self._session.query(Citizen)
                       .filter_by(citizen_id=citizen_id)
                       .first())

    def delete_by_citizen_id(self, citizen_id: int) -> None:
        log.debug(f"Deleting citizen with {citizen_id = }")

        (self._session.query(Citizen)
                      .filter_by(citizen_id=citizen_id)
                      .delete())
