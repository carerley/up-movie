from abc import abstractmethod

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Requestor:
    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    @abstractmethod
    def request(self, method, url, params=None, **kwargs):
        pass
