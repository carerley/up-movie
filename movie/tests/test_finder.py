import os, sys
from unittest import TestCase

from movie.finder import AMC_DETAILS_PAGE_LINK_SELECTOR, TitleFinder, AMC_TITLE_SELECTOR, AMC_INTERNATIONAL_FILM_URL

WEB_DRIVER_PATH = os.getenv("WEB_DRIVER_PATH")


class TestFinder(TestCase):
    def test_find_all_titles(self):
        titles = TitleFinder.zen_row_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)

    def test_selenium_find_all_titles(self):
        finder = TitleFinder()
        page = finder.selenium_find_all_detail_pages(base_url=AMC_INTERNATIONAL_FILM_URL, page_link_selector=AMC_DETAILS_PAGE_LINK_SELECTOR)
        title = finder.selenium_find_title_from_detail_page(page)
        print(title)
        # assert len(pages) > 0
        # for page in pages:
        #     title = finder.selenium_find_title_from_detail_page(page)
        #     print(title)

    def test_selenium_find_all_names(self):
        names = TitleFinder.selenium_find_all_titles(base_url="https://www.medicare.gov/care-compare/", title_selector=".ProviderSearchMenuListing__label")
        print(names)

    def test_chrome_in_path(self):
        sys.path.append(WEB_DRIVER_PATH)
        print(sys.path)
        


