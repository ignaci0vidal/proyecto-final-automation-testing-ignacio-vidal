from pages.login_page import LoginPage


def login_valido(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")