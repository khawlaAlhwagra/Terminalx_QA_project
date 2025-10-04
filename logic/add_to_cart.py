from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    REMOVE_BTNS = "div.cart-item_3yl1 button.remove_wqPe"  # כל כפתורי ההסרה

    def __init__(self, browser):
        self._browser = browser

    def remove_first_item(self):
        # לוקח את הכפתור הראשון ומוחק אותו
        remove_btn = WebDriverWait(self._browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.REMOVE_BTNS))
        )
        remove_btn.click()

        # מחכה שהכפתור הראשון ייעלם → הפריט נמחק
        WebDriverWait(self._browser, 15).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.REMOVE_BTNS))
        )
        return True
