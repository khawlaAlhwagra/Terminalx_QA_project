import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.invald_login_terminalx import LoginTerminalx
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RemoveFavoriteTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/women?auth=login")

    def test_remove_from_favorites(self):
        # כניסה לחשבון
        login_page = LoginTerminalx(self.browser)
        login_page.fill_user_email_input("khawla06777@gmail.com")
        login_page.fill_password_input("12345678Kf#")
        login_page.click_login_button()
        time.sleep(3)

        # מעבר לעמוד המועדפים
        self.browser.get("https://www.terminalx.com/wishlist/items")
        wait = WebDriverWait(self.browser, 15)

        # איתור כל כפתורי REMOVE (אם יש)
        remove_buttons = self.browser.find_elements(By.XPATH, '//button[text()="REMOVE"]')
        if not remove_buttons:
            self.fail("אין מוצרים במועדפים להסרה")

        # שמירה על המספר הראשוני של פריטים
        before = len(remove_buttons)

        # לחיצה על הראשון
        remove_buttons[0].click()

        # המתנה שהפריט יוסר או שהמספר ישתנה
        try:
            wait.until(lambda d: len(d.find_elements(By.XPATH, '//button[text()="REMOVE"]')) < before)
            removed = True
        except TimeoutException:
            removed = False

        self.assertTrue(removed, "המוצר לא הוסר מהרשימה או שהעמוד לא עודכן")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
