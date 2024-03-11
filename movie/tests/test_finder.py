from unittest import TestCase

from movie.finder import Finder, AMC_TITLE_SELECTOR, AMC_INTERNATIONAL_FILM_URL


class TestFinder(TestCase):
    def test_find_all_titles(self):
        titles = Finder.zen_row_find_all_titles(base_url=AMC_INTERNATIONAL_FILM_URL, title_selector=AMC_TITLE_SELECTOR)
        assert len(titles) > 0
        print(titles)


