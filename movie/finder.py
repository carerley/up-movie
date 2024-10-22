import os
import sys
from typing import List

from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from movie.requestor import Requestor
from movie.web_requestor import WebRequestor, ZenRowWebRequestor

AMC_TITLE_SELECTOR = ".PosterContent a h3"
AMC_DETAILS_PAGE_LINK_SELECTOR = ".PosterContent a:first-child"
AMC_DETAILS_PAGE_TITLE_SELECTOR = "h1.headline-paused"
AMC_DOMAIN = "www.amctheatres.com"
AMC_INTERNATIONAL_FILM_URL = f"https://{AMC_DOMAIN}/programs/international-films"
WEB_DRIVER_PATH = os.getenv("WEB_DRIVER_PATH")


class TitleFinder:
    def __init__(self) -> None:
        sys.path.append(WEB_DRIVER_PATH)
        self.driver = webdriver.Chrome()

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

    @DeprecationWarning
    def selenium_find_all_titles(self, base_url: str, title_selector: str) -> list[str]:
        """Doesn't work for AMC page as it returns a lot of empty titles. """
    
        self.driver.get(base_url)
        elements = self.driver.find_elements(By.CSS_SELECTOR, title_selector)
        titles = []
        for element in elements:
            titles.append(element.text)

        return titles

    def selenium_find_all_detail_pages(self, base_url: str, page_link_selector: str) -> WebElement:
        self.driver.implicitly_wait(10) # seconds
        self.driver.get(base_url)
        self.driver.implicitly_wait(10) # seconds
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, page_link_selector))
        # )
        # return element
        return self.driver.find_element(by=By.CSS_SELECTOR, value=page_link_selector)

    def selenium_find_title_from_detail_page(self, pageElement: WebElement) -> str:
        pageElement.click()
        element = self.driver.find_element(By.CSS_SELECTOR, AMC_DETAILS_PAGE_TITLE_SELECTOR)
        return element.text

    @classmethod
    def __find_all_titles(cls, requestor: Requestor, base_url: str, title_selector: str) -> list[str]:
        response = requestor.request(method="GET", url=base_url)
        tree = html.fromstring(response.content)
        elements = tree.cssselect(title_selector)
        titles = []
        for element in elements:
            titles.append(element.text)

        return titles
