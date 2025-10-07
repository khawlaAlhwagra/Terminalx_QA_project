import time
from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    SIZE_OPTION = '//div[@data-test-id="qa-size-item" and text()="M"]'
    ADD_TO_CART_BTN = '//button[@data-test-id="qa-add-to-cart-button"]'
    MINI_CART_PRODUCT_NAME = '//a[@data-test-id="qa-minicart-product-name"]'
    MINI_CART_SIZE = '//span[@data-test-id="qa-item-size-value"]'
    MINI_CART_COLOR = '//span[@data-test-id="qa-item-color-value"]'
    MINI_CART_PRICE = '//div[contains(@class,"price_cQfM")]'
    MINI_CART_QTY = '//select[@class="select_zdc5 rtl_62yk qty-select_RbvK"]'
    MINI_CART_ICON = '//a[@data-test-id="qa-link-minicart"]'  # אייקון סל

    def __init__(self, browser):
        super().__init__(browser)

    def select_size_m(self):
        size_m = WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SIZE_OPTION))
        )
        size_m.click()
        time.sleep(1)

    def add_to_cart(self):
        add_btn = WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_BTN))
        )
        add_btn.click()
        time.sleep(2)

    def get_minicart_product_name(self):
        name = WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MINI_CART_PRODUCT_NAME))
        )
        return name.text

    def get_minicart_size(self):
        size = WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MINI_CART_SIZE))
        )
        return size.text

    def get_minicart_color(self):
        color = WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MINI_CART_COLOR))
        )
        return color.text

    def get_minicart_price(self):
        price = WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MINI_CART_PRICE))
        )
        return price.text

    def get_minicart_qty(self):
        qty = WebDriverWait(self._browser, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MINI_CART_QTY))
        )
        return qty.get_attribute("value")

    def verify_item_added_to_cart(self):
        """בודק שהמוצר נוסף לסל בהצלחה"""
        try:
            WebDriverWait(self._browser, 10).until(
                EC.presence_of_element_located((By.XPATH, self.MINI_CART_PRODUCT_NAME))
            )
            print(" המוצר נוסף לסל בהצלחה")
            return True
        except:
            print(" המוצר לא נוסף לסל")
            return False
