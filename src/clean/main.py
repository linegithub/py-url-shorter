from src.macarronic.url_shorter import UrlShorter

def main():
    shortened_url_1 = UrlShorter.shorturl(
        "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview"
    )
    shortened_url_2 = UrlShorter.shorturl(
        "https://developer.mozilla.org/en-US/docs/"
    )

    shortened_url_3 = UrlShorter.shorturl(
        "https://yahoo.com/mail"
    )

    print(f"shortened url {shortened_url_1.short_url}")
    print(f"shortened url {shortened_url_2.short_url}")
    print(f"shortened url {shortened_url_3.short_url}")