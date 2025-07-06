import logging

logger = logging.getLogger("flight_catalog")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

# Mostrar en consola
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
