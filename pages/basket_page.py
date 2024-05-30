from base.base_page import BasePage
from .locators import AddToBasketLocators
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage,AddToBasketLocators):

    def add_laptop_to_basket(self):
        self.wait.until(EC.element_to_be_clickable(self.ButtonAddToCartLaptop)).click()

    def go_to_basket(self):
        self.wait.until(EC.element_to_be_clickable(self.ShoppingCart)).click()

    def agree_with_terms(self):
        self.wait.until(EC.element_to_be_clickable(self.TermsOfService)).click()
        self.wait.until(EC.element_to_be_clickable(self.CheckoutButton)).click()

    def checkout_as_guest(self):
        self.wait.until(EC.element_to_be_clickable(self.CheckoutAsGuest)).click()

    def create_new_address(self):
        self.wait.until(EC.element_to_be_clickable(self.FirstName)).send_keys("Billy")
        self.wait.until(EC.element_to_be_clickable(self.LastName)).send_keys("Juli")
        self.wait.until(EC.element_to_be_clickable(self.Email)).send_keys("Billy@mail.ru")
        self.wait.until(EC.element_to_be_clickable(self.CountrySelect)).click()
        self.wait.until(EC.element_to_be_clickable(self.ChooseUAS)).click()
        self.wait.until(EC.element_to_be_clickable(self.City)).send_keys("LA")
        self.wait.until(EC.element_to_be_clickable(self.Address1)).send_keys("LA st2")
        self.wait.until(EC.element_to_be_clickable(self.Zip)).send_keys("234")
        self.wait.until(EC.element_to_be_clickable(self.PhoneNumber)).send_keys("+234")
        self.wait.until(EC.element_to_be_clickable(self.ContinueButton)).click()

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.ContinueButton2)).click()
        self.wait.until(EC.element_to_be_clickable(self.ContinueButton3)).click()
        self.wait.until(EC.element_to_be_clickable(self.ContinueButton4)).click()
        self.wait.until(EC.element_to_be_clickable(self.ContinueButton5)).click()
        self.wait.until(EC.element_to_be_clickable(self.ConfirmButton)).click()

    def order_should_be_created(self):
        text_order = "Your order has been successfully processed!"
        title =self.wait.until(EC.element_to_be_clickable(self.OrderTitle)).text
        assert title==text_order, \
            print(title)








