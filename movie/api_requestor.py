import os

from dotenv import load_dotenv

from movie.requestor import Requestor


class AmcApiRequestor(Requestor):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.base_url = "https://api.amctheatres.com"

    def request(self, method, url, params=None, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["X-AMC-Vendor-Key"] = self.api_key

        response = self.session.request(method, self.base_url + url, params=params, headers=headers)
        response.raise_for_status()
        return response
