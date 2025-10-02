from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoTerminalx(BasePage):
    # Generic locator that should match common logo patterns
    # You mentioned a generic XPath is acceptable
    LOGO = '//*[contains(@class, "logo") or contains(@id, "logo")]'

    def __init__(self, browser):
        super().__init__(browser)

    def get_logo_element(self):
        """Wait for and return the logo WebElement."""
        return WebDriverWait(self._browser, 15).until(
            EC.presence_of_element_located((By.XPATH, self.LOGO))
        )

    def is_logo_displayed(self):
        """Return True if the logo element is displayed on the page."""
        try:
            el = WebDriverWait(self._browser, 15).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGO))
            )
            return el.is_displayed()
        except Exception:
            return False