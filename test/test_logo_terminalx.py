import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.logo_terminalx import LogoTerminalx


class LogoDisplayTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/")

    def test_verify_homepage_logo_displayed(self):
        logo_page = LogoTerminalx(self.browser)

        # Optional brief wait to allow visual stability
        time.sleep(1)

        # Verify the logo is displayed on the homepage
        self.assertTrue(
            logo_page.is_logo_displayed(),
            "TerminalX logo is not displayed on the homepage"
        )

        time.sleep(1)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()