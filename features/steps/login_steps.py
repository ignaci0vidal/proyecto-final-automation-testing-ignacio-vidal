from behave import given, when, then

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger


@given(
    "que el usuario está en la página de login"
)
def step_abrir_pagina_login(context):
    logger.info(
        "Abriendo la página de login desde Behave"
    )

    context.login_page = LoginPage(
        context.driver
    )
    context.inventory_page = InventoryPage(
        context.driver
    )

    context.login_page.abrir()


@when(
    'ingresa el usuario "{usuario}" '
    'y la contraseña "{password}"'
)
def step_ingresar_credenciales(
    context,
    usuario,
    password
):
    logger.info(
        "Ingresando credenciales BDD para %s",
        usuario
    )

    context.login_page.completar_usuario(
        usuario
    )
    context.login_page.completar_password(
        password
    )
    context.login_page.hacer_click_login()


@then("debe acceder al inventario")
def step_validar_inventario(context):
    logger.info(
        "Validando acceso al inventario desde BDD"
    )

    assert "inventory.html" in (
        context.driver.current_url
    )

    assert (
        context.inventory_page.obtener_titulo()
        == "Products"
    )

    assert (
        context.inventory_page
        .obtener_cantidad_productos()
        > 0
    )


@then(
    "debe visualizar un mensaje "
    "de usuario bloqueado"
)
def step_validar_usuario_bloqueado(context):
    logger.info(
        "Validando mensaje de usuario bloqueado"
    )

    mensaje = (
        context.login_page
        .obtener_mensaje_error()
    )

    assert "locked out" in mensaje.lower()