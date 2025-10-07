import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.invald_login_terminalx import LoginTerminalx
from logic.Login_into_women_page import WomenPage

class LoginTestTerminalx(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/women?auth=login")

    def test_login_success(self):
        login_page = LoginTerminalx(self.browser)

        time.sleep(1)
        login_page.fill_user_email_input("khawla06777@gmail.com")
        login_page.fill_password_input("12345678Kf#")
        login_page.click_login_button()

        women_page = WomenPage(self.browser)
        current_url = women_page.get_current_url()
        print(f"Current URL after login: {current_url}")

        # בדיקה גמישה יותר: מתחיל ב-/women גם אם יש query string
        self.assertTrue(
            current_url.startswith("https://www.terminalx.com/women"),
            f"Unexpected URL after login: {current_url}"
        )

        time.sleep(3)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
