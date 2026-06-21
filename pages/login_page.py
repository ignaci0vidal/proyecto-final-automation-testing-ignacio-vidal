from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USER_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def completar_usuario(self, usuario):
        campo_usuario = self.wait.until(
            EC.visibility_of_element_located(self.USER_INPUT)
        )
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

    def completar_password(self, password):
        campo_password = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        campo_password.clear()
        campo_password.send_keys(password)

    def hacer_click_login(self):
        boton_login = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        boton_login.click()

    def login(self, usuario, password):
        self.abrir()
        self.completar_usuario(usuario)
        self.completar_password(password)
        self.hacer_click_login()

    def obtener_mensaje_error(self):
        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return mensaje.text