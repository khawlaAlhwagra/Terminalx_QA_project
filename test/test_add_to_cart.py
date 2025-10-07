import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.AddproductToCART_page import ProductPage
from logic.invald_login_terminalx import LoginTerminalx


class TestAddToCart(unittest.TestCase):

    def setUp(self):
        """פתיחת דפדפן וכניסה לעמוד התחברות"""
        login_url = "https://www.terminalx.com/women?auth=login"
        self.browser = BrowserWrapper().get_driver(login_url)
        self.login_page = LoginTerminalx(self.browser)

    def tearDown(self):
        """סגירת הדפדפן אחרי כל טסט"""
        self.browser.quit()

    def test_add_to_cart(self):
        """בדיקה מלאה - כניסה לחשבון + הוספת מוצר לעגלה"""

        # כניסה לחשבון
        self.login_page.fill_user_email_input("khawla06777@gmail.com")
        self.login_page.fill_password_input("12345678Kf#")
        self.login_page.click_login_button()
        time.sleep(3)

        # מעבר לדף מוצר
        product_url = "https://www.terminalx.com/default-category/w655950008?color=7"
        self.browser.get(product_url)
        self.product_page = ProductPage(self.browser)

        # בחירת מידה
        self.product_page.select_size_m()

        # הוספה לסל
        self.product_page.add_to_cart()

        # אימות שהמוצר נוסף לסל
        is_added = self.product_page.verify_item_added_to_cart()
        self.assertTrue(is_added, "המוצר לא נוסף לסל בהצלחה")

        # הדפסה לוודוא
        product_name = self.product_page.get_minicart_product_name()
        print(f" מוצר שנוסף לסל: {product_name}")

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
