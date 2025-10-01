class BasePage:

    def __init__(self, browser):
        self._browser = browser

    def get_current_url(self):
        return self._browser.current_url
