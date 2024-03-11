import os
from typing import Any, Iterable
from urllib.parse import urlencode

import scrapy
from dotenv import load_dotenv
from scrapy import Request
from scrapy.http import Response

AMC_TITLE_TEXT_SELECTOR = ".PosterContent a h3::text"
AMC_DOMAIN = "www.amctheatres.com"
AMC_INTERNATIONAL_FILM_URL = f"https://{AMC_DOMAIN}/programs/international-films"


def get_zen_row_url(url: str, api_key: str) -> str:
    payload = {
        'url': url
    }

    return f'https://api.zenrows.com/v1/?apikey={api_key}&{urlencode(payload)}'


class AmcSpider(scrapy.Spider):
    """
    Script file for scrapy to find movie titles. Note that this is an isolate script file independent of package
    movie to avoid throwing an exception.
    """
    name = "amc"
    allowed_domains = [AMC_DOMAIN]
    start_urls = [AMC_INTERNATIONAL_FILM_URL]

    def __init__(self, **kwargs: Any):
        load_dotenv()
        self.zen_row_api_key = os.getenv("ZEN_ROW_API_KEY")
        super().__init__(**kwargs)

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield Request(url=get_zen_row_url(url=url, api_key=self.zen_row_api_key), callback=self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        titles = response.css(AMC_TITLE_TEXT_SELECTOR).getall()
        for title in titles:
            yield {"title": title}
