from unittest import TestCase

from movie.finder import TitleFinder, AMC_TITLE_SELECTOR, AMC_INTERNATIONAL_FILM_URL


class TestFinder(TestCase):
    def test_find_all_titles(self):
        titles = TitleFinder.zen_row_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)

    def test_selenium_find_all_titles(self):
        finder = TitleFinder()
        titles = finder.selenium_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)
        print("done")

    def test_selenium_find_all_titles_library(self):
        base_url = "https://queenslibrary.org"
        title_selector = ".title a"
        finder = TitleFinder()
        titles = finder.selenium_find_all_titles(base_url, title_selector)
        assert len(titles) > 0
        for title in titles:
            print(title)
        


