import unittest

from datetime import datetime

from src.clean.infrastructure.datasource.in_memory_data_source import InMemoryDataSource
from tests.mocks.url_shorter_mocks import UrlShorterMocks


class InMemoryDataSourceTest(unittest.TestCase) :

    def test_save_single_item(self):
        short_url_dictionary = UrlShorterMocks.empty_persistence_dictionary()
        repo = InMemoryDataSource(
            storage_dict= short_url_dictionary
        )
        item = UrlShorterMocks.mock_empty_dto_item()

        result = repo.save(item)

        self.assertTrue(result)

        print(short_url_dictionary)

        self.assertTrue(
            item.short_url in short_url_dictionary
        )

        self.assertEqual(
            first = short_url_dictionary[item.short_url],
             second = item
        )

    def test_delete_by_object(self):
        short_url_dictionary = UrlShorterMocks.empty_persistence_dictionary()
        repo = InMemoryDataSource(
            storage_dict=short_url_dictionary
        )
        item = UrlShorterMocks.mock_empty_dto_item()

        short_url_dictionary[item.short_url] = item
        result = repo.delete_by_object(item_to_delete= item)

        self.assertTrue(result)
        self.assertTrue(item.short_url not in short_url_dictionary)

if __name__ == '__main__':
    unittest.main()
