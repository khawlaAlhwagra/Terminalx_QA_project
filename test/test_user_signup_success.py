import unittest
import time
import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from infra.browser_wrapper import BrowserWrapper
from logic.signup_terminalx import SignupPage

class TestSignupTerminalx(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://www.terminalx.com/women"
        self.browser = BrowserWrapper.get_driver(self.base_url)
        self.wait = WebDriverWait(self.browser, 25)

    def _generate_email(self):
        rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"auto_{int(time.time())}_{rand}@example.com"

    def test_signup_flow(self):
        page = SignupPage(self.browser)
        email = self._generate_email()
        password = "Test@12345"
        first_name = "בשיר"
        last_name = "אבו גאמה"
        phone = "0501234567"

        self.assertTrue(page.open_login_modal(), "❌ לא הצליח ללחוץ על כפתור התחברות")
        time.sleep(1)
        self.assertTrue(page.switch_to_signup_tab(), "❌ לא הצליח לעבור ללשונית הרשמה")
        time.sleep(1)
        self.assertTrue(page.fill_signup_form(email, password, first_name, last_name, phone), "❌ מילוי הטופס נכשל")
        time.sleep(1)
        self.assertTrue(page.submit_form(), "❌ שליחת הטופס נכשלה")
        time.sleep(5)  # לראות את התוצאה

    def tearDown(self):
        print("[✓] סוגר את הדפדפן...")
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()