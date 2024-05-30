from base.base_page import BasePage
from .locators import CheckFilterLocators
from selenium.webdriver.support import expected_conditions as EC

class JewelryPage(BasePage,CheckFilterLocators):

    def go_to_jewelry_page(self):
        self.wait.until(EC.element_to_be_clickable(self.Jewelry)).click()

    def sorted_by_A_to_Z(self):
        self.wait.until(EC.element_to_be_clickable(self.SortBy)).click()
        self.wait.until(EC.element_to_be_clickable(self.AtoZ)).click()

    def should_be_sorted_A_to_Z(self):
        firstItem =self.wait.until(EC.element_to_be_clickable(self.FirstBookPrice)).text
        lastItem=self.wait.until(EC.element_to_be_clickable(self.LastBookPrice)).text
        assert firstItem[0] > lastItem[-1], \
            f"Incorrect sort"