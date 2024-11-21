# logging_config.py
import logging

from colorama import Fore, Style, init

# Initialize colorama for colored logs
init(autoreset=True)


# Custom formatter for different log levels
class CustomFormatter(logging.Formatter):
    LOG_COLORS = {
        logging.INFO: Fore.GREEN,
        logging.ERROR: Fore.RED,
        logging.WARNING: Fore.YELLOW,
        logging.DEBUG: Fore.BLUE,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        # Set the log color based on the level
        log_color = self.LOG_COLORS.get(record.levelno, Fore.WHITE)

        # Override the log level format
        log_format = f"{Fore.CYAN}[%(asctime)s]{Style.RESET_ALL} {log_color}%(levelname)s{Style.RESET_ALL}: %(message)s"

        # Use the parent class to format the record with the new log format
        formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


# Configure logging
def setup_logger():
    # Create a logger
    logger = logging.getLogger(__name__)

    # Prevent adding multiple handlers
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Add custom formatter to the handler
        ch.setFormatter(CustomFormatter())

        # Add handler to logger
        logger.addHandler(ch)

    return logger
