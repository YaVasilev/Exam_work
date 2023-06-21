import time

from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
from .Pages.login_page import LoginPage

import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_product_page()
#     page.should_be_basket_btn()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_about_adding()
#     page.should_be_message_basket_total()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()


# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_be_message_disappeared_after_adding_product_to_basket()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#     page = ProductPage(browser, link)
#     page.open()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_basket_empty()
#     basket_page.should_be_empty_message()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = LoginPage.generate_password(self, 10)
        page.register_new_user(email, password)
        page.user_login_to_account()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
