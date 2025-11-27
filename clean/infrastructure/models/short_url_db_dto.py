from dataclasses import dataclass
from datetime import datetime

@dataclass
class ShortUrlPersistenceDTO:
    short_url: str
    long_url: str
    created_at: datetime
    updated_at: datetime