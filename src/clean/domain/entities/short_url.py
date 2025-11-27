from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ShortUrl:
    short_url: str
    long_url: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(cls, long_url, short_url):
        now = datetime.now()
        return cls(short_url, long_url, now, now)