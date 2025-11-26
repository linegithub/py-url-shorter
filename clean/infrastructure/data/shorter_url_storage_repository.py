from typing import List

from clean.domain.entities.short_url import ShortUrl
from clean.domain.contracts.repository.i_shorter_url_storage_repository import ShorterUrlStorageRepositoryInterface
from clean.infrastructure.data_source.i_data_source import DataSourceInterface

class ShorterUrlStorageRepository(ShorterUrlStorageRepositoryInterface):

    def __init__(
            self,
            data_source: DataSourceInterface,
    ):
        self.data_source = data_source

    def insert_short_url(self, short_url: ShortUrl) -> object:
        result = self.data_source.save(
            item_to_save = short_url
        )
        return result

    def get_short_url(self, short_url_id: str) -> ShortUrl:
        short_url = self.data_source.get(
            item_id=short_url_id
        )
        return short_url

    def delete_short_url(self, short_url_id: str) -> bool:
        result = self.data_source.delete_by_id(
            item_id_to_delete=short_url_id
        )
        return result


    def get_all_short_urls(self) -> List[ShortUrl]:
        list_of_short_urls = self.data_source.get_all()
        return list_of_short_urls
