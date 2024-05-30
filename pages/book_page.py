from base.base_page import BasePage
from .locators import CheckFilterLocators
from selenium.webdriver.support import expected_conditions as EC

class BookPage(BasePage,CheckFilterLocators):

    def go_to_book_page(self):
        self.wait.until(EC.element_to_be_clickable(self.Books)).click()

    def sorted_by_high_to_low(self):
        self.wait.until(EC.element_to_be_clickable(self.SortBy)).click()
        self.wait.until(EC.element_to_be_clickable(self.HighToLow)).click()

    def should_be_correct_sort(self):
        firstBook =self.wait.until(EC.element_to_be_clickable(self.FirstBookPrice)).text
        lastBook=self.wait.until(EC.element_to_be_clickable(self.LastBookPrice)).text
        assert float(firstBook) > float(lastBook), \
            f"{firstBook}!>{lastBook}"


