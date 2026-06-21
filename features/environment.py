import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger import logger


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)

    logger.info(
        "Iniciando escenario BDD: %s",
        scenario.name
    )


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshots_dir = pathlib.Path(
            "reports/screenshots/behave"
        )
        screenshots_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        screenshot_path = (
            screenshots_dir
            / f"{scenario.name.replace(' ', '_')}.png"
        )

        context.driver.save_screenshot(
            str(screenshot_path)
        )

        logger.error(
            "Escenario BDD fallido. Captura guardada en %s",
            screenshot_path
        )

    context.driver.quit()

    logger.info(
        "Finalizando escenario BDD: %s",
        scenario.name
    )