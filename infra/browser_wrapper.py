from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserWrapper:
    @staticmethod
    def get_driver(url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(url)
        return driver
