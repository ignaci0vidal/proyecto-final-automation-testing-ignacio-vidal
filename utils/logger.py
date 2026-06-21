import logging
import pathlib
from datetime import datetime


logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #Windows no permite : dentro de nombres de archivos.

logging.basicConfig(
    filename=logs_dir / f"automation_{timestamp}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)

logger = logging.getLogger("automation_testing")