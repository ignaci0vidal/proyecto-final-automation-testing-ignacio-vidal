import pathlib

from utils.driver_factory import crear_driver
from utils.logger import logger


def before_scenario(context, scenario):
    context.driver = crear_driver()

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

        nombre_archivo = (
            scenario.name
            .replace(" ", "_")
            .replace("/", "_")
        )

        screenshot_path = (
            screenshots_dir
            / f"{nombre_archivo}.png"
        )

        context.driver.save_screenshot(
            str(screenshot_path)
        )

        logger.error(
            "Escenario BDD fallido. "
            "Captura guardada en %s",
            screenshot_path
        )

    context.driver.quit()

    logger.info(
        "Finalizando escenario BDD: %s",
        scenario.name
    )