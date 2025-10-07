import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.invald_login_terminalx import LoginTerminalx
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToFavorites(unittest.TestCase):

    def setUp(self):
        # פתיחת דפדפן וכניסה לעמוד התחברות
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/women?auth=login")

        # התחברות לחשבון
        login_page = LoginTerminalx(self.browser)
        time.sleep(1)
        login_page.fill_user_email_input("khawla06777@gmail.com")
        login_page.fill_password_input("12345678Kf#")
        login_page.click_login_button()

        # המתנה לטעינה מלאה
        WebDriverWait(self.browser, 15).until(EC.url_contains("women"))
        time.sleep(2)

    def test_add_to_favorites(self):
        """בדיקה שהמשתמש יכול להוסיף מוצר למועדפים (אהוב)"""
        wait = WebDriverWait(self.browser, 15)

        # פתיחת עמוד מוצר
        self.browser.get("https://www.terminalx.com/default-category/w789555913?vog=32753&color=9172")
        time.sleep(3)

        # לחיצה על כפתור "MY LIST"
        add_to_favorites = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'MY LIST')]"))
        )
        add_to_favorites.click()
        time.sleep(3)

        # מעבר לעמוד המועדפים
        self.browser.get("https://www.terminalx.com/wishlist/items")
        time.sleep(3)

        # בדיקה שהמוצר נוסף
        items = self.browser.find_elements(By.CSS_SELECTOR, "li.wishlist-product_2rk- a.title_3ZxJ")
        found = any("ג'ינס" in item.text for item in items)

        self.assertTrue(found, "❌ המוצר לא נוסף למועדפים (אהוב)")
        print("✅ הבדיקה עברה בהצלחה — המוצר נוסף לרשימת האהובים!")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
