import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser = webdriver.Edge(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()