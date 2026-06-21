import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
def test_agregar_backpack_al_carrito(login_in_driver):
    logger.info("Iniciando test_agregar_backpack_al_carrito")

    driver = login_in_driver

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    logger.info("Agregando Sauce Labs Backpack al carrito")
    inventory_page.agregar_backpack_al_carrito()

    logger.info("Validando contador del carrito")
    assert inventory_page.obtener_cantidad_carrito() == "1"

    logger.info("Abriendo carrito")
    inventory_page.abrir_carrito()

    logger.info("Validando producto dentro del carrito")
    assert "cart.html" in driver.current_url
    assert "Sauce Labs Backpack" in cart_page.obtener_nombres_productos()

    logger.info("test_agregar_backpack_al_carrito finalizado correctamente")


@pytest.mark.ui
def test_eliminar_backpack_del_carrito(login_in_driver):
    logger.info("Iniciando test_eliminar_backpack_del_carrito")

    driver = login_in_driver

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.agregar_backpack_al_carrito()
    inventory_page.abrir_carrito()

    logger.info("Eliminando Sauce Labs Backpack del carrito")
    cart_page.eliminar_backpack()

    logger.info("Validando carrito vacío")
    assert cart_page.obtener_cantidad_productos() == 0

    logger.info("test_eliminar_backpack_del_carrito finalizado correctamente")