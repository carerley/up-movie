import os
from urllib.parse import urlencode

from dotenv import load_dotenv

from movie.requestor import Requestor


class WebRequestor(Requestor):
    """
    Simple requestor to use User Agent headers to act like a web browser.
    """

    def request(self, method, url, params=None, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["User-Agent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                                 "like Gecko) Chrome/122.0.0.0 Safari/537.36")
        headers["Referer"] = "https://www.google.com/"
        response = self.session.request(method, url, params=params, headers=headers)
        response.raise_for_status()
        return response


class ZenRowWebRequestor(Requestor):
    """
    Zen row web requestor to handle requests to scrape some data from website. Zen row proxy the website url to solve
    403 issues.
    """
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.zen_row_api_key = os.getenv("ZEN_ROW_API_KEY")

    def request(self, method, url, params=None, **kwargs):
        response = self.session.request(method, self.__get_zen_row_url(url), params=params)
        response.raise_for_status()
        return response

    def __get_zen_row_url(self, url: str) -> str:
        payload = {
            'url': url
        }
        return f'https://api.zenrows.com/v1/?apikey={self.zen_row_api_key}&{urlencode(payload)}'
