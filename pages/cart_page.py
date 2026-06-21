from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombres_productos(self):
        elementos = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.ITEM_NAMES
            )
        )

        return [elemento.text for elemento in elementos]

    def obtener_cantidad_productos(self):
        productos = self.driver.find_elements(
            *self.CART_ITEMS
        )
        return len(productos)

    def eliminar_backpack(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_BACKPACK_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            boton
        )

        boton.click()

        self.wait.until(
            EC.invisibility_of_element_located(
                self.REMOVE_BACKPACK_BUTTON
            )
        )