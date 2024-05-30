from selenium.webdriver.common.by import By


class AddToBasketLocators():
    ButtonAddToCartLaptop = (By.XPATH, '''//input[@onclick="AjaxCart.addproducttocart_catalog('/addproducttocart/catalog/31/1/1    ');return false;"]''')
    ShoppingCart = (By.XPATH, '//a[contains(text(), "shopping cart")]')
    TermsOfService = (By.XPATH, '//input[@id="termsofservice"]')
    CheckoutButton = (By.XPATH, '//button[contains(text(), "Checkout")]')
    CheckoutAsGuest = (By.XPATH, '//input[@value="Checkout as Guest"]')
    FirstName = (By.XPATH, '//input[@id="BillingNewAddress_FirstName"]')
    LastName = (By.XPATH, '//input[@id="BillingNewAddress_LastName"]')
    Email = (By.XPATH, '//input[@id="BillingNewAddress_Email"]')
    CountrySelect = (By.XPATH, '//select[@id="BillingNewAddress_CountryId"]')
    ChooseUAS = (By.XPATH, '//option[@value="1"]')
    City = (By.XPATH, '//input[@id="BillingNewAddress_City"]')
    Address1 = (By.XPATH, '//input[@id="BillingNewAddress_Address1"]')
    Zip = (By.XPATH, '//input[@id="BillingNewAddress_ZipPostalCode"]')
    PhoneNumber = (By.XPATH, '//input[@id="BillingNewAddress_PhoneNumber"]')
    ContinueButton = (By.XPATH, '//input[@title="Continue"][@onclick="Billing.save()"]')
    ContinueButton2 = (By.XPATH, '//input[@title="Continue"][@onclick="Shipping.save()"]')
    ContinueButton3 = (By.XPATH, '//input[@onclick="ShippingMethod.save()"]')
    ContinueButton4 = (By.XPATH, '//input[@onclick="PaymentMethod.save()"]')
    ContinueButton5 = (By.XPATH, '//input[@onclick="PaymentInfo.save()"]')
    ConfirmButton = (By.XPATH, '//input[@onclick="ConfirmOrder.save()"]')
    OrderTitle = (By.XPATH, '//div[@class="title"]/strong')

class CheckFilterLocators():
    Books = (By.XPATH, """//li[@class="inactive"]/a[contains(text(), 'Books')]""")
    SortBy= (By.XPATH, '//select[@id="products-orderby"]')
    HighToLow = (By.XPATH, "//option[contains(text(), 'High to Low')]")
    FirstBookPrice = (By.XPATH, '(//span[@class="price actual-price"])[1]')
    LastBookPrice = (By.XPATH, '(//span[@class="price actual-price"])[last()]')

    Jewelry = (By.XPATH, """//li[@class="inactive"]/a[contains(text(), 'Jewelry')]""")
    AtoZ = (By.XPATH, "//option[contains(text(), 'A to Z')]")
    FirstJewelryItem = (By.XPATH, '(//h2/a)[1]')
    LastJewelryItem = (By.XPATH, '(//h2/a)[last()]')

class CompareLocators():
    Books = (By.XPATH, """//li[@class="inactive"]/a[contains(text(), 'Books')]""")
    CompAndInt = (By.XPATH, "//a[text()='Computing and Internet']")
    CopyCompAndInt = (By.XPATH, "//a[contains(text(), 'Copy of Computing and Internet')]")
    AddToCompareButton =(By.XPATH, '//input[@value = "Add to compare list"]')
    PriceFirstItem = (By.XPATH, "(//tr[@class='product-price']/td)[2]")
    PriceSecondItem = (By.XPATH, "(//tr[@class='product-price']/td)[3]")

class ReviewLocators():
    LogIn= (By.XPATH, '//a[text()="Log in"]')
    Email =(By.XPATH, '//input[@id="Email"]')
    Password = (By.XPATH, '//input[@id="Password"]')
    ButtonLogIn=(By.XPATH,'//input[@value="Log in"]')
    Laptop = (By.XPATH, '//img[@src="https://demowebshop.tricentis.com/content/images/thumbs/0000224_141-inch-laptop_125.png"]')
    AddReview =(By.XPATH, '//a[text()="Add your review"]')
    ReviewTitle = (By.XPATH, '//input[@id="AddProductReview_Title"]')
    ReviewText = (By.XPATH, '//textarea[@id="AddProductReview_ReviewText"]')
    SubmitReview = (By.XPATH, '//input[@name="add-review"]')
    Result = (By.XPATH, '//div[@class="result"]')



