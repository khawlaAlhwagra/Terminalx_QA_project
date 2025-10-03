import unittest
from logic.browser_wrapper import BrowserWrapper
from logic.favorites_page import FavoritesPage


class TestAddToFavorites(unittest.TestCase):
    def setUp(self):
        # פותח דפדפן עם ה־wrapper שלך
        self.browser = BrowserWrapper().get_driver("https://www.terminalx.com/catalogsearch/result?department_level=11221&product_list_order=justlanded&q=%D7%92%27%D7%99%D7%A0%D7%A1")
        self.favorites_page = FavoritesPage(self.browser)

    def test_add_from_catalog(self):
        """
        בדיקה שמשתמש יכול להוסיף מוצר למועדפים מעמוד קטלוג
        """
        result = self.favorites_page.add_from_catalog()
        self.assertTrue(result, "לא הצליח להוסיף למועדפים מעמוד קטלוג")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
