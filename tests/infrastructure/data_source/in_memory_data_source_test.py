import pytest

from clean.infrastructure.datasource.dictionary import short_url_dictionary
from clean.infrastructure.datasource.in_memory_data_source import InMemoryDataSource

from tests.test_mocks import mock_item

@pytest.fixture(scope="class", autouse=True)
def class_setup():
    print("Resetando dict para a classe inteira")
    short_url_dictionary.clear()
    yield
    print("Finalizou classe")

class InMemoryDataSourceTest :

    def test_save(self):
        repo = InMemoryDataSource()
        item = mock_item

        result = repo.save(item)

        assert result is True
        assert item.short_url in short_url_dictionary
        assert short_url_dictionary[item.short_url] is item

    def test_delete_by_object(self):
        repo = InMemoryDataSource()
        item = mock_item

        short_url_dictionary[item.short_url] = item
        result = repo.delete_by_object(item_to_delete= item)

        assert result is True
        assert item.short_url not in short_url_dictionary
