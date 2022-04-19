from abc import ABC, abstractmethod
from api.domain.dtos import Citizen
from typing import Optional


class AbstractCitizenRepository(ABC):
    @abstractmethod
    def save(self, citizen: Citizen) -> None:
        pass

    @abstractmethod
    def find_by_citizen_id(self, citizen_id: int) -> Optional[Citizen]:
        pass

    @abstractmethod
    def delete_by_citizen_id(self, citizen_id: int) -> None:
        pass

