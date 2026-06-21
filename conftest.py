import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.saucedemo_helpers import login_valido


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    navegador = webdriver.Chrome(options=options) #para abrir chrome, en caso de usar otro browser, cambiar
    navegador.implicitly_wait(5)

    yield navegador

    navegador.quit()


@pytest.fixture
def login_in_driver(driver):
    login_valido(driver)
    return driver