from typing import List

from clean.domain.interfaces.data_source.i_data_source import DataSourceInterface

class DataSourceInterfaceImpl(DataSourceInterface):

    def __init__(
            self,
            data_source: DataSourceInterface,
    ):
        self.data_source = data_source

    def save(self, item_to_save: object) -> bool:
        pass

    def delete_by_object(self, item_to_delete: object) -> bool:
        pass

    def delete_by_id(self, item_id_to_delete: str) -> bool:
        pass

    def get(self, item_id: str) -> object:
        pass

    def get_by_long_url(self, long_url: str) -> object:
        pass

    def get_all(self) -> List[object]:
        pass