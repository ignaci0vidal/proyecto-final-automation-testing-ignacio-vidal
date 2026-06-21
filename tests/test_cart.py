import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.smoke
def test_agregar_backpack_al_carrito(login_in_driver):
    driver = login_in_driver

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.agregar_backpack_al_carrito()

    assert inventory_page.obtener_cantidad_carrito() == "1" #valido que el badge sea 1, es decir que agregó al carrito    

    inventory_page.abrir_carrito()  #abro el carrito

    assert "cart.html" in driver.current_url #valido url
    assert "Sauce Labs Backpack" in (
        cart_page.obtener_nombres_productos()
    )


@pytest.mark.ui
def test_eliminar_backpack_del_carrito(login_in_driver):
    driver = login_in_driver

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.agregar_backpack_al_carrito() #agrega el producto al carrito
    inventory_page.abrir_carrito()

    cart_page.eliminar_backpack()

    assert cart_page.obtener_cantidad_productos() == 0