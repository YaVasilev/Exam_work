from .Base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Подстроки login нет в URL"

    def should_be_login_form(self):
        enter_login_field = self.browser.find_element(*LoginPageLocators.ENTER_LOGIN_FIELD)
        enter_login_field.click()
        assert self.is_element_present(*LoginPageLocators.ENTER_LOGIN_FIELD), "Enter login field is not presented"

        enter_pass_field = self.browser.find_element(*LoginPageLocators.ENTER_PASS_FIELD)
        enter_pass_field.click()
        assert self.is_element_present(*LoginPageLocators.ENTER_PASS_FIELD), "Enter password field is not presented"

        enter_btn = self.browser.find_element(*LoginPageLocators.ENTER_BTN)
        # enter_btn.click()
        assert self.is_element_present(*LoginPageLocators.ENTER_BTN), "Enter button is not presented"
    def should_be_register_form(self):
        reg_login_field = self.browser.find_element(*LoginPageLocators.REG_LOGIN_FIELD)
        reg_login_field.click()
        assert self.is_element_present(*LoginPageLocators.ENTER_LOGIN_FIELD), "Registration login field is not presented"

        reg_pass1_field = self.browser.find_element(*LoginPageLocators.REG_PASS1_FIELD)
        reg_pass1_field.click()
        assert self.is_element_present(*LoginPageLocators.REG_PASS1_FIELD), "Registration password field is not presented"

        reg_pass2_field = self.browser.find_element(*LoginPageLocators.REG_PASS2_FIELD)
        reg_pass2_field.click()
        assert self.is_element_present(*LoginPageLocators.REG_PASS2_FIELD), "Registration accept field is not presented"

        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        # reg_btn.click()
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Registration button is not presented"