from unittest import TestCase

from movie.finder import TitleFinder, AMC_TITLE_SELECTOR, AMC_INTERNATIONAL_FILM_URL


class TestFinder(TestCase):
    def test_find_all_titles(self):
        titles = TitleFinder.zen_row_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)

    def test_selenium_find_all_titles(self):
        titles = TitleFinder.selenium_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)


