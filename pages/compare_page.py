from base.base_page import BasePage
from .locators import CompareLocators,ReviewLocators
from selenium.webdriver.support import expected_conditions as EC

class ComparePage(BasePage,CompareLocators):

    def go_to_book_page(self):
        self.wait.until(EC.element_to_be_clickable(self.Books)).click()

    def add_computing_and_internet(self):
        self.wait.until(EC.element_to_be_clickable(self.CompAndInt)).click()
        self.wait.until(EC.element_to_be_clickable(self.AddToCompareButton)).click()

    def add_copy_of_computing_and_internet(self):
        self.wait.until(EC.element_to_be_clickable(self.CopyCompAndInt)).click()
        self.wait.until(EC.element_to_be_clickable(self.AddToCompareButton)).click()

    def should_be_same_price(self):
        first_item =self.wait.until(EC.element_to_be_clickable(self.PriceFirstItem)).text
        second_item =self.wait.until(EC.element_to_be_clickable(self.PriceSecondItem)).text
        assert float(first_item)==float(second_item), \
        "Wrong value"

class ReviewPage(BasePage,ReviewLocators):

    def log_in(self):
        self.wait.until(EC.element_to_be_clickable(self.LogIn)).click()
        self.wait.until(EC.element_to_be_clickable(self.Email)).send_keys("wdq@mail.ru")
        self.wait.until(EC.element_to_be_clickable(self.Password)).send_keys("123456")
        self.wait.until(EC.element_to_be_clickable(self.ButtonLogIn)).click()

    def choose_laptop(self):
        self.wait.until(EC.element_to_be_clickable(self.Laptop)).click()

    def review(self):
        self.wait.until(EC.element_to_be_clickable(self.AddReview)).click()
        self.wait.until(EC.element_to_be_clickable(self.ReviewTitle)).send_keys("some text")
        self.wait.until(EC.element_to_be_clickable(self.ReviewText)).send_keys("some text")
        self.wait.until(EC.element_to_be_clickable(self.SubmitReview)).click()

    def should_review_created(self):
        result = self.wait.until(EC.element_to_be_clickable(self.Result)).text
        assert result == "Product review is successfully added.", \
        f"{result}"

