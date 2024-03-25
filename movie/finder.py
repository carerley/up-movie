import os

from lxml import html
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import ArgOptions

from movie.requestor import Requestor
from movie.web_requestor import WebRequestor, ZenRowWebRequestor

AMC_TITLE_SELECTOR = ".PosterContent a h3"
AMC_DOMAIN = "www.amctheatres.com"
AMC_INTERNATIONAL_FILM_URL = f"https://{AMC_DOMAIN}/programs/international-films"
WEB_DRIVER_PATH = os.getenv("WEB_DRIVER_PATH")


class TitleFinder:
    @classmethod
    def find_all_titles(cls, base_url: str, title_selector: str) -> list[str]:
        """
        Find movie titles on website by css selector.
        :param base_url: base url for website that display movies
        :param title_selector: selector of movie titles
        :return: list of movie titles
        """
        return cls.__find_all_titles(WebRequestor(), base_url, title_selector)

    @classmethod
    @DeprecationWarning
    def zen_row_find_all_titles(cls, base_url: str, title_selector: str) -> list[str]:
        """
        Zen row requires subscription >$49/month.
        Same as find_all_titles but use 3p lib zen row to generate urls that can be scraped.
        """
        return cls.__find_all_titles(ZenRowWebRequestor(), base_url, title_selector)

    @classmethod
    def selenium_find_all_titles(cls, base_url: str, title_selector: str) -> list[str]:
        """use selenium to drive a browser to scrape element like human. """
        webdriver.Options
        driver = webdriver.ChromiumDriver(options={"driver_path": WEB_DRIVER_PATH})
        driver.get(base_url)
        elements = driver.find_elements(By.CSS_SELECTOR, title_selector)
        titles = []
        for element in elements:
            titles.append(element.text)

        return titles

    @classmethod
    def __find_all_titles(cls, requestor: Requestor, base_url: str, title_selector: str) -> list[str]:
        response = requestor.request(method="GET", url=base_url)
        tree = html.fromstring(response.content)
        elements = tree.cssselect(title_selector)
        titles = []
        for element in elements:
            titles.append(element.text)

        return titles
