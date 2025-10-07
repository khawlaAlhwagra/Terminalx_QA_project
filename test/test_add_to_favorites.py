import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_to_favorites import FavoritesPage

class TestAddToFavorites(unittest.TestCase):

    def setUp(self):
        url = "https://www.terminalx.com/default-category/w789555913?vog=32753&color=9172"
        self.browser = BrowserWrapper().get_driver(url)
        self.favorites_page = FavoritesPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_add_to_favorites(self):
        result = self.favorites_page.add_to_favorites()
        self.assertTrue(result, " Failed to add item to favorites")
