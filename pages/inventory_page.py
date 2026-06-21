from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    REMOVE_BACKPACK_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def obtener_titulo(self):
        titulo = self.wait.until(
            EC.visibility_of_element_located(
                self.TITLE
            )
        )

        return titulo.text

    def obtener_cantidad_productos(self):
        productos = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.INVENTORY_ITEMS
            )
        )

        return len(productos)

    def agregar_backpack_al_carrito(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BACKPACK_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            boton
        )

        boton.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.REMOVE_BACKPACK_BUTTON
                )
            )

        except TimeoutException:
            boton = self.wait.until(
                EC.presence_of_element_located(
                    self.ADD_BACKPACK_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                boton
            )

            self.wait.until(
                EC.visibility_of_element_located(
                    self.REMOVE_BACKPACK_BUTTON
                )
            )

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.CART_BADGE,
                "1"
            )
        )

    def obtener_cantidad_carrito(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        )

        return badge.text

    def abrir_carrito(self):
        carrito = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            carrito
        )

        carrito.click()

        try:
            self.wait.until(
                EC.url_contains("cart.html")
            )

        except TimeoutException:
            carrito = self.wait.until(
                EC.presence_of_element_located(
                    self.CART_LINK
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                carrito
            )

            self.wait.until(
                EC.url_contains("cart.html")
            )