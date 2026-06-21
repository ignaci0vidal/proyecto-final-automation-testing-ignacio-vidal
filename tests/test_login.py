import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.smoke

#primer test, happy path
def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.obtener_cantidad_productos() > 0

#segundo test, test negativo
@pytest.mark.ui
def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)

    login_page.login("locked_out_user", "secret_sauce")

    mensaje_error = login_page.obtener_mensaje_error()

    assert "locked out" in mensaje_error.lower()