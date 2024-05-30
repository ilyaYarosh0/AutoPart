from pages.basket_page import BasketPage
from pages.book_page import BookPage
from pages.jewelry_page import JewelryPage
from pages.compare_page import ComparePage,ReviewPage


def test_add_to_basket(browser):
    url="https://demowebshop.tricentis.com/"
    basket_page = BasketPage(browser, url)
    basket_page.open()
    basket_page.add_laptop_to_basket()
    basket_page.go_to_basket()
    basket_page.agree_with_terms()
    basket_page.checkout_as_guest()
    basket_page.create_new_address()
    basket_page.confirm_order()
    basket_page.order_should_be_created()

def test_sort_books_high_to_low(browser):
    url = "https://demowebshop.tricentis.com/"
    book_page = BookPage(browser, url)
    book_page.open()
    book_page.go_to_book_page()
    book_page.sorted_by_high_to_low()
    book_page.should_be_correct_sort()

def test_sort_jewelry_A_to_Z(browser):
    url = "https://demowebshop.tricentis.com/"
    jewelry_page = JewelryPage(browser, url)
    jewelry_page.open()
    jewelry_page.go_to_jewelry_page()
    jewelry_page.sorted_by_A_to_Z()
    jewelry_page.should_be_sorted_A_to_Z()

def test_compare_books(browser):
    url = "https://demowebshop.tricentis.com/"
    compare_page= ComparePage(browser,url)
    compare_page.open()
    compare_page.go_to_book_page()
    compare_page.add_computing_and_internet()
    compare_page.go_to_book_page()
    compare_page.add_copy_of_computing_and_internet()
    compare_page.should_be_same_price()

def test_review(browser):
    url = "https://demowebshop.tricentis.com/"
    review_page = ReviewPage(browser, url)
    review_page.open()
    review_page.log_in()
    review_page.choose_laptop()
    review_page.review()
    review_page.should_review_created()