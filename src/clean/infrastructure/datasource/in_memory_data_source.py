from typing import List

from src.clean.domain.interfaces.data_source.i_data_source import DataSourceInterface
from src.clean.infrastructure.models.short_url_db_dto import ShortUrlPersistenceDTO

class InMemoryDataSource(DataSourceInterface):

    def __init__(self, storage_dict: dict[str, ShortUrlPersistenceDTO]):
        self.short_url_dictionary = storage_dict

    def save(self, item_to_save: ShortUrlPersistenceDTO) -> bool:
        self.short_url_dictionary[item_to_save.short_url] = item_to_save
        return item_to_save.short_url in self.short_url_dictionary

    def delete_by_object(self, item_to_delete: ShortUrlPersistenceDTO) -> bool:
        del self.short_url_dictionary[item_to_delete.short_url]
        return item_to_delete.short_url not in self.short_url_dictionary

    def delete_by_id(self, short_url_id: str) -> bool:
        del self.short_url_dictionary[short_url_id]
        return short_url_id not in self.short_url_dictionary

    def get(self, short_url_id: str) -> ShortUrlPersistenceDTO:
        return self.short_url_dictionary[short_url_id]

    def get_by_long_url(self, long_url: str) -> ShortUrlPersistenceDTO:
        pass

    def get_all(self) -> List[ShortUrlPersistenceDTO]:
        pass