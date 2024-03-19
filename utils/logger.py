# Logging utility
# utils/logger.py - Logging utility

import logging
from logging.handlers import RotatingFileHandler
import os

# Define the base directory for log files
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log file path
log_file = os.path.join(log_dir, "sapphire.log")

# Configure logging
logger = logging.getLogger("S.A.P.P.H.I.R.E.")
logger.setLevel(logging.DEBUG)  # Set to logging.INFO in production

# Create handlers: one for the console and one for the file with rotation
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=5)

# Set logging level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Create logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log(message, level=logging.INFO):
    """
    Utility function to log messages. Default level is INFO.
    """
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        logger.info(message)

# Example usage
# if __name__ == "__main__":
#     log("This is a test message.", logging.DEBUG)
