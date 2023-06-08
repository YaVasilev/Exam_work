from .Pages.Main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.locators import LoginPageLocators


from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    go_to_login_page(browser)
    page.should_be_login_page()
