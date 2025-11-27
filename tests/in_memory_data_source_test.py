import unittest

from datetime import datetime

from src.clean.infrastructure.datasource.in_memory_data_source import InMemoryDataSource
from src.clean.infrastructure.models.short_url_db_dto import ShortUrlPersistenceDTO

def empty_mock_item() -> ShortUrlPersistenceDTO:
    return ShortUrlPersistenceDTO(
        short_url="abc123",
        long_url="http://www.google.com",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


def clean_storage_dict() -> dict[str, ShortUrlPersistenceDTO]:
    """Empty mock dictionary."""
    return {}


class InMemoryDataSourceTest(unittest.TestCase) :

    def test_save(self):
        short_url_dictionary = clean_storage_dict()
        repo = InMemoryDataSource(
            storage_dict= {}
        )
        item = empty_mock_item()

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
        short_url_dictionary = clean_storage_dict()
        repo = InMemoryDataSource(
            storage_dict=short_url_dictionary
        )
        item = empty_mock_item()

        short_url_dictionary[item.short_url] = item
        result = repo.delete_by_object(item_to_delete= item)

        self.assertTrue(result)
        self.assertTrue(item.short_url not in short_url_dictionary)

if __name__ == '__main__':
    unittest.main()
