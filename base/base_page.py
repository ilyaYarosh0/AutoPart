from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url=url
        self.wait=WebDriverWait(browser, 10, poll_frequency=1)

    def open(self):
        self.browser.get(self.url)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.url))
