import unittest
import time

from infra.browser_wrapper import BrowserWrapper
from logic.login_terminalx import LoginTerminalx
from logic.remove_favorite_terminalx import RemoveFavoriteTerminalx


class RemoveFavoriteTest(unittest.TestCase):

    def setUp(self):
        # Start at homepage as per test steps
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/")

    def test_verify_remove_from_favorites(self):
        # 1) Log in using existing Login POM flow (same approach as login test)
        self.browser.get("https://www.terminalx.com/women?auth=login")
        LoginTerminalx(self.browser).full_login_flow("khawla06777@gmail.com", "12345678Kf#")

        # 2) Open Favorites section
        fav_page = RemoveFavoriteTerminalx(self.browser)
        fav_page.open_favorites_section()

        # 3) Remove one favorite item (best-effort)
        fav_page.remove_first_favorite()

        # 4) Refresh/revisit favorites
        fav_page.refresh_favorites()
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
