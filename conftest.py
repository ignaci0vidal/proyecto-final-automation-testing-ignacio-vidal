import pathlib

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger import logger
from utils.saucedemo_helpers import login_valido


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    navegador = webdriver.Chrome(options=options)
    navegador.implicitly_wait(5)

    logger.info("Navegador Chrome iniciado")

    yield navegador

    navegador.quit()
    logger.info("Navegador Chrome cerrado")


@pytest.fixture
def login_in_driver(driver):
    logger.info("Ejecutando login válido desde fixture")
    login_valido(driver)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = pathlib.Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            screenshot_path = screenshots_dir / f"{item.name}.png"

            driver.save_screenshot(str(screenshot_path))

            logger.error(
                "El test %s falló. Captura guardada en %s",
                item.name,
                screenshot_path
            )

            extras = getattr(report, "extras", [])
            screenshot_base64 = driver.get_screenshot_as_base64()

            extras.append(
                pytest_html.extras.png(
                    screenshot_base64,
                    name=f"Screenshot - {item.name}"
                )
            )

            report.extras = extras