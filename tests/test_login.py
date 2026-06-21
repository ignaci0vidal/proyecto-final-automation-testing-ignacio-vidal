import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
def test_login_exitoso(driver):
    logger.info("Iniciando test_login_exitoso")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    logger.info("Ingresando con usuario standard_user")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Validando acceso al inventario")
    assert "inventory.html" in driver.current_url
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.obtener_cantidad_productos() > 0

    logger.info("test_login_exitoso finalizado correctamente")


@pytest.mark.ui
def test_login_usuario_bloqueado(driver):
    logger.info("Iniciando test_login_usuario_bloqueado")

    login_page = LoginPage(driver)

    logger.info("Intentando ingresar con locked_out_user")
    login_page.login("locked_out_user", "secret_sauce")

    mensaje_error = login_page.obtener_mensaje_error()

    logger.info("Validando mensaje de usuario bloqueado")
    assert "locked out" in mensaje_error.lower()

    logger.info(
        "test_login_usuario_bloqueado finalizado correctamente"
    )