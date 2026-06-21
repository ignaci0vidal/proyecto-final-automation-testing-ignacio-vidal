import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    navegador = webdriver.Chrome(options=options) #para abrir Chorme, en caso de usar otro cambiar
    navegador.implicitly_wait(5)

    yield navegador

    navegador.quit()