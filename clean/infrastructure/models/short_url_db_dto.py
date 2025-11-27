from dataclasses import dataclass
from datetime import datetime

@dataclass
class ShortUrl:
    short_url: str
    long_url: str
    created_at: datetime
    updated_at: datetime