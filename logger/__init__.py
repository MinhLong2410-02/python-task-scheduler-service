import logging
from logger.color import CustomFormatter
def setup_logging():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # or any other level

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter
    ch.setFormatter(CustomFormatter())

    # Add handler to logger
    logger.addHandler(ch)