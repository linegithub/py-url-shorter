from typing import List

from clean.domain.interfaces.data_source.i_data_source import DataSourceInterface
from clean.infrastructure.datasource.dictionary import short_url_dictionary
from clean.infrastructure.models.short_url_db_dto import ShortUrlPersistenceDTO


class InMemoryDataSource(DataSourceInterface):

    def save(self, item_to_save: ShortUrlPersistenceDTO) -> bool:
        short_url_dictionary[item_to_save.short_url] = item_to_save
        return item_to_save.short_url in short_url_dictionary

    def delete_by_object(self, item_to_delete: ShortUrlPersistenceDTO) -> bool:
        del short_url_dictionary[item_to_delete.short_url]
        return item_to_delete.short_url not in short_url_dictionary

    def delete_by_id(self, short_url_id: str) -> bool:
        del short_url_dictionary[short_url_id]
        return short_url_id not in short_url_dictionary

    def get(self, short_url_id: str) -> ShortUrlPersistenceDTO:
        return short_url_dictionary[short_url_id]

    def get_by_long_url(self, long_url: str) -> ShortUrlPersistenceDTO:
        pass

    def get_all(self) -> List[ShortUrlPersistenceDTO]:
        pass