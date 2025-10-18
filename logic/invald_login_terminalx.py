from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTerminalx(BasePage):
    LOGIN_MODAL_BUTTON = '//button[contains(text(), "התחברות")]'
    USER_EMAIL_INPUT = '//input[@id="qa-login-email-input"]'
    PASSWORD_INPUT = '//input[@id="qa-login-password-input"]'
    LOGIN_BUTTON = '//button[contains(@class, "submit-btn")]'
    ERROR_MESSAGE = '//div[contains(@class, "error-message_")]'
    def __init__(self, browser):
        super().__init__(browser)

    def open_login_modal(self):
        print("[+] Trying to click on login button")
        try:
            login_btn = WebDriverWait(self._browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="qa-header-login-button"]'))
            )
            login_btn.click()
            print("[✓] Clicked on 'התחברות' button")
            return True
        except Exception as e:
            print("[!] Failed to click on login button:", e)
            return False

    def fill_user_email_input(self, email):
        WebDriverWait(self._browser, 5).until(
            EC.presence_of_element_located((By.XPATH, self.USER_EMAIL_INPUT))
        ).send_keys(email)

    def fill_password_input(self, password):
        WebDriverWait(self._browser, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT))
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self._browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))
        ).click()

    def login_with_invalid_credentials(self, email, password):
        if not self.open_login_modal():
            return ""

        self.fill_user_email_input(email)
        self.fill_password_input(password)
        self.click_login_button()

        try:
            error_el = WebDriverWait(self._browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE))
            )
            return error_el.text.strip()
        except:
            return ""