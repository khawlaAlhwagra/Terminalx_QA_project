import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.invald_login_terminalx import LoginTerminalx
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RemoveFromCartTest(unittest.TestCase):

    def setUp(self):
        # פתיחת דפדפן וכניסה לעמוד ההתחברות
        self.browser = BrowserWrapper.get_driver("https://www.terminalx.com/women?auth=login")

    def test_remove_from_cart(self):
        """בדיקה שמוודאת שניתן להסיר מוצר מהסל הראשי לאחר כניסה למערכת"""

        # כניסה למערכת
        login_page = LoginTerminalx(self.browser)
        login_page.fill_user_email_input("khawla06777@gmail.com")
        login_page.fill_password_input("12345678Kf#")
        login_page.click_login_button()
        time.sleep(4)

        wait = WebDriverWait(self.browser, 20)

        # מעבר לעמוד הסל הראשי
        self.browser.get("https://www.terminalx.com/checkout/cart")
        print(" נפתח עמוד הסל הראשי")
        time.sleep(4)

        #  איתור כרטיסי מוצרים
        items = self.browser.find_elements(By.CSS_SELECTOR, "div.container_1XqK")
        if not items:
            self.fail(" אין מוצרים בסל למחיקה")

        before_count = len(items)
        print(f" מספר מוצרים לפני מחיקה: {before_count}")

        # ⃣ מציאת כפתור מחיקה של הפריט הראשון
        try:
            remove_button = items[0].find_element(By.CSS_SELECTOR, "button.remove_wqPe")
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", remove_button)
            time.sleep(1)
            self.browser.execute_script("arguments[0].click();", remove_button)
            print(" לחיצה על כפתור המחיקה בוצעה בהצלחה")
        except Exception as e:
            self.fail(f" שגיאה בלחיצה על כפתור המחיקה: {e}")

        # ️המתנה לטעינת דף חדשה או ירידה בכמות הפריטים
        try:
            wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "div.container_1XqK")) < before_count)
            removed = True
        except TimeoutException:
            removed = False

        # ️ בדיקה אם ההסרה בוצעה
        self.assertTrue(removed, " הפריט לא הוסר מהסל או שהעמוד לא עודכן")
        print(" הבדיקה עברה בהצלחה — הפריט הוסר מהסל!")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
