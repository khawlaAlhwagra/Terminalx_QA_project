import time
from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginTerminalx(BasePage):
    USER_EMAIL_INPUT = '//input[@id="qa-login-email-input"]'
    PASSWORD_INPUT = '//input[@id="qa-login-password-input"]'
    LOGIN_BUTTON = '//button[@class="tx-link-a submit-btn_2LDW tx-link_29YD btn_1UzJ btn-yellow_2tf3 uppercase_1KUt"]'

    def __init__(self, browser):
        super().__init__(browser)
        self._user_email_input = self._browser.find_element(By.XPATH, self.USER_EMAIL_INPUT)
        self._password_input = self._browser.find_element(By.XPATH, self.PASSWORD_INPUT)

    def fill_user_email_input(self, user_email):
        self._user_email_input.send_keys(user_email)
        time.sleep(1)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)
        time.sleep(1)

    def click_login_button(self):
        login_button = WebDriverWait(self._browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))
        )
        try:
            login_button.click()
        except Exception:
            self._browser.execute_script("arguments[0].click();", login_button)
        time.sleep(2)

    def full_login_flow(self, user_email, password):
        self.fill_user_email_input(user_email)
        self.fill_password_input(password)
        self.click_login_button()
