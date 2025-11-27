from abc import abstractmethod, ABC
from typing import List

from src.clean.infrastructure.models.short_url_db_dto import ShortUrlPersistenceDTO

class DataSourceInterface(ABC):

    @abstractmethod
    def save(self, item_to_save : ShortUrlPersistenceDTO) -> bool:
        ...

    @abstractmethod
    def delete_by_object(self, item_to_delete:object) -> bool:
        ...

    @abstractmethod
    def delete_by_id(self, item_id_to_delete: str) -> bool:
        ...

    @abstractmethod
    def get(self, item_id:str) -> object:
        ...

    @abstractmethod
    def get_by_long_url(self, long_url:str) -> object:
        ...

    @abstractmethod
    def get_all(self) -> List[object]:
        ...