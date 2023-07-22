from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ID_LOGIN_USERNAME = (By.ID, "id_login-username")
    ID_LOGIN_PASSWORD = (By.ID, "id_login-password")
    ID_LOGIN_BUTTON = (By.NAME, "login_submit")

    ID_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    ID_REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    ID_REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    ID_REGISTRATION_BUTTON = (By.NAME, "registration_submit")