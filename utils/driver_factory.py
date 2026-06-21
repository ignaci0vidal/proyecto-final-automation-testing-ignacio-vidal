import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crear_driver():
    options = Options()
    options.add_argument("--start-maximized")

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=options)
    navegador.implicitly_wait(5)

    return navegador