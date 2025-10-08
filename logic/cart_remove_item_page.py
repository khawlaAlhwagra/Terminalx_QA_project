from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
import time


class CartRemoveItemPage(BasePage):
    CART_ICON = (By.CSS_SELECTOR, "a[data-test-id='qa-link-minicart']")
    CART_COUNT = (By.CSS_SELECTOR, "a[data-test-id='qa-link-minicart'] span.item-count_3Yeu")
    MINI_CART_CONTAINER = (By.CSS_SELECTOR, "div.minicart-items_2W6O")
    CART_ITEM = (By.CSS_SELECTOR, "div.item-wrap_8n9Y")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a[data-test-id='qa-minicart-product-name']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.remove_wqPe")
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[contains(text(),'אין מוצרים בסל') or contains(text(),'עגלה ריקה')]")

    def open_cart(self):
        cart_icon = WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
        WebDriverWait(self._browser, 10).until(
            EC.visibility_of_element_located(self.MINI_CART_CONTAINER)
        )

    def get_cart_count(self):
        try:
            count_text = WebDriverWait(self._browser, 5).until(
                EC.presence_of_element_located(self.CART_COUNT)
            ).text.strip()
            return int(count_text) if count_text.isdigit() else 0
        except Exception:
            return 0

    def get_item_titles(self):
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_all_elements_located(self.CART_ITEM)
        )
        items = self._browser.find_elements(*self.PRODUCT_NAME)
        return [i.text.strip() for i in items if i.text.strip()]

    def remove_first_item(self):
        WebDriverWait(self._browser, 10).until(
            EC.presence_of_all_elements_located(self.REMOVE_BUTTON)
        )
        remove_buttons = self._browser.find_elements(*self.REMOVE_BUTTON)
        if not remove_buttons:
            raise Exception("❌ לא נמצא כפתור מחיקה בסל")

        remove_buttons[0].click()
        time.sleep(2)
        print("🗑️ בוצעה לחיצה על הסרת הפריט הראשון")

    def is_cart_empty(self):
        try:
            WebDriverWait(self._browser, 3).until(
                EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)
            )
            return True
        except Exception:
            items = self._browser.find_elements(*self.CART_ITEM)
            return len(items) == 0
