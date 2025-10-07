from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FavoritesPage:
    MY_LIST_BTN = "span.info-text_2dWq"  # הסלקטור של הכפתור "MY LIST"

    def __init__(self, browser):
        self._browser = browser

    def add_to_favorites(self):
        """
        לוחץ על הכפתור 'MY LIST' כדי להוסיף מוצר למועדפים
        """
        btn = WebDriverWait(self._browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.MY_LIST_BTN))
        )
        btn.click()
        return True
