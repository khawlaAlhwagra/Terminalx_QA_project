import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.invald_login_terminalx import LoginTerminalx

class LoginTestTerminalx(unittest.TestCase):

    def test_login_invalid_credentials(self):
        """Verify error message appears when using invalid login credentials."""
        driver = BrowserWrapper.get_driver("https://www.terminalx.com")
        page = LoginTerminalx(driver)
        try:
            error_text = page.login_with_invalid_credentials(
                email="invalid@example.com",
                password="WrongPassword123"
            )
            self.assertTrue(error_text, "❌ לא הופיעה הודעת שגיאה למרות התחברות עם פרטים לא נכונים")
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()