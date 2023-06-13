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

class ProductPageLocators():
#Кнопка добавить в корзину
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
#Alert о добавлении товара в корзину
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
#Название товара
    PRODUCT_TITTLE = (By.CSS_SELECTOR, "div.product_main h1")
#Сумма в корзине
    MESSAGE_BASKET_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
#Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


