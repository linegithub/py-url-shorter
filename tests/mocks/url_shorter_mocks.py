from datetime import datetime

from src.clean.infrastructure.models.short_url_db_dto import ShortUrlPersistenceDTO

class UrlShorterMocks:

    @staticmethod
    def mock_empty_dto_item() -> ShortUrlPersistenceDTO:
        return ShortUrlPersistenceDTO(
            short_url="abc123",
            long_url="http://www.google.com",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    @staticmethod
    def empty_persistence_dictionary() -> dict[str, ShortUrlPersistenceDTO]:
        """Empty mock dictionary."""
        return {}