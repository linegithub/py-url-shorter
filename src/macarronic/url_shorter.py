from sqids import Sqids

from src.clean.domain.entities.short_url import ShortUrl
from src.macarronic.get_last_url import get_last_id

class UrlShorter:

    def shorturl(long_url:str):
        sqids = Sqids()
        short_url = sqids.encode(numbers=[get_last_id()])
        obj_short_url = ShortUrl.create(
            long_url=long_url,
            short_url = short_url
        )

        return obj_short_url