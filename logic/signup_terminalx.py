import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)

    def open_login_modal(self):
        print("[+] Trying to click on login button")
        try:
            login_btn = self.browser.find_element(By.CSS_SELECTOR, "[data-test-id='qa-header-login-button']")
            login_btn.click()
            print("[✓] Clicked on 'התחברות' button")
            return True
        except Exception as e:
            print("[!] Failed to click on login button:", e)
            return False

    def switch_to_signup_tab(self):
        print("[+] Trying to switch to 'הרשמה' tab")
        try:
            signup_tab = self.browser.find_element(By.XPATH, "//div[contains(@class,'tab_ZRBF') and text()='הרשמה']")
            signup_tab.click()
            print("[✓] Clicked on 'הרשמה' tab")
            return True
        except Exception as e:
            print("[!] Failed to click on 'הרשמה' tab:", e)
            return False

    def fill_signup_form(self, email, password, first_name, last_name, phone, birthdate="01/01/1995"):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "qa-register-email-input"))).send_keys(email)
            self.browser.find_element(By.ID, "qa-register-password-input").send_keys(password)
            self.browser.find_element(By.ID, "qa-register-firstname-input").send_keys(first_name)
            self.browser.find_element(By.ID, "qa-register-lastname-input").send_keys(last_name)
            self.browser.find_element(By.XPATH, "//input[@placeholder='מספר טלפון']").send_keys(phone)
            self.browser.find_element(By.ID, "qa-register-date_of_birth-input").send_keys(birthdate)

            # בחירת מין - נשים
            self.browser.find_element(By.CSS_SELECTOR, "input[name='women']").click()

            # תיבת סימון: קבלת פרסומים
            self.browser.find_element(By.NAME, "is_subscribed").click()

            # תיבת סימון: תנאי שימוש
            self.browser.find_element(By.XPATH, "//label[contains(., 'תנאי השימוש')]//input[@type='checkbox']").click()

            print("[✓] Filled signup form")
            return True
        except Exception as e:
            print("[!] Failed to fill signup form:", e)
            return False

    def submit_form(self):
        try:
            # איתור הכפתור שוב למניעת stale element
            submit_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-btn_1KTI"))
            )
            self.browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
            print("[✓] Submitted signup form")
            return True
        except Exception as e:
            print("[!] Failed to submit signup form:", e)
            return False