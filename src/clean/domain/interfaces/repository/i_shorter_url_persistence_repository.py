from abc import abstractmethod, ABC
from src.clean.domain.entities.short_url import ShortUrl

class ShorterUrlPersistenceRepositoryInterface(ABC):

    @abstractmethod
    def insert_short_url(self, short_url : str) -> bool:
        ...

    @abstractmethod
    def get_short_url(self, url_id: str) -> ShortUrl:
        ...

    @abstractmethod
    def get_short_url_str(self, long_url: str) -> str:
        ...

    @abstractmethod
    def delete_short_url(self, short_url: int) -> str:
        ...

    @abstractmethod
    def get_all_short_urls(self, ) -> []:
        ...