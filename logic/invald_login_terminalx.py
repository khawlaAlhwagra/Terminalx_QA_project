from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTerminalx(BasePage):
    USER_EMAIL_INPUT = '//input[@id="qa-login-email-input"]'
    PASSWORD_INPUT = '//input[@id="qa-login-password-input"]'
    LOGIN_BUTTON = '//button[@class="tx-link-a submit-btn_2LDW tx-link_29YD btn_1UzJ btn-yellow_2tf3 uppercase_1KUt"]'

    def __init__(self, browser):
        super().__init__(browser)

    def fill_user_email_input(self, user_email):
        WebDriverWait(self._browser, 5).until(
            EC.presence_of_element_located((By.XPATH, self.USER_EMAIL_INPUT))
        ).send_keys(user_email)

    def fill_password_input(self, password):
        WebDriverWait(self._browser, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT))
        ).send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self._browser, 7).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON))
        )
        try:
            login_button.click()
        except Exception:
            self._browser.execute_script("arguments[0].click();", login_button)

    def full_login_flow(self, user_email, password):
        self.fill_user_email_input(user_email)
        self.fill_password_input(password)
        self.click_login_button()


def login_with_invalid_credentials(driver, email, password):
    driver.get("https://www.terminalx.com/login")

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, LoginTerminalx.USER_EMAIL_INPUT))
    ).send_keys(email)

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, LoginTerminalx.PASSWORD_INPUT))
    ).send_keys(password)

    login_btn = WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.XPATH, LoginTerminalx.LOGIN_BUTTON))
    )
    try:
        login_btn.click()
    except Exception:
        driver.execute_script("arguments[0].click();", login_btn)

    error_locators = [
        (By.XPATH, '//*[@data-test-id="qa-login-error" or @data-testid="qa-login-error"]'),
        (By.XPATH, '//*[@role="alert"]'),
    ]
    for by, sel in error_locators:
        try:
            el = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((by, sel))
            )
            text = (el.text or '').strip()
            if text:
                return text
        except Exception:
            continue

    return ""