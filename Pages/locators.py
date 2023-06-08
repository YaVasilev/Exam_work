from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    ENTER_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_PASS_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    ENTER_BTN = (By.CSS_SELECTOR, "#login_form > button")

    REG_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "#register_form > button")

