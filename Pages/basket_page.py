from .Base_page import BasePage
from .locators import BasketLocators
class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.browser.is_element_present(*BasketLocators.BASKET_EMPTY_PRODUCT), "Basket is not empty"

    def should_be_empty_message(self):
        message = self.browser.is_element_present(*BasketLocators.BASKET_IS_EMPTY).text
        assert message in "Continue shopping", "Basket message about empty is not exist"