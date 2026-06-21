import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import obtener_casos_login
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.smoke
def test_login_exitoso(driver):
    logger.info("Iniciando test_login_exitoso")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.obtener_cantidad_productos() > 0

    logger.info("test_login_exitoso finalizado correctamente")


@pytest.mark.ui
@pytest.mark.parametrize(
    "usuario,password,resultado_esperado",
    obtener_casos_login()
)
def test_login_con_datos_csv(
    driver,
    usuario,
    password,
    resultado_esperado
):
    logger.info(
        "Ejecutando login parametrizado con usuario %s",
        usuario
    )

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(usuario, password)

    if resultado_esperado == "success":
        assert "inventory.html" in driver.current_url
        assert inventory_page.obtener_titulo() == "Products"

    elif resultado_esperado == "locked":
        mensaje_error = login_page.obtener_mensaje_error()

        assert "locked out" in mensaje_error.lower()

    elif resultado_esperado == "error":
        mensaje_error = login_page.obtener_mensaje_error()

        assert "username and password do not match" in (
            mensaje_error.lower()
        )

    else:
        pytest.fail(
            f"Resultado esperado no reconocido: "
            f"{resultado_esperado}"
        )