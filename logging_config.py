# logging_config.py
import logging
from colorama import Fore, Style, init

# Initialize colorama for colored logs
init(autoreset=True)

# Configure logging
def setup_logger():
    logging.basicConfig(
        format=f"{Fore.CYAN}[%(asctime)s]{Style.RESET_ALL} {Fore.YELLOW}%(levelname)s{Style.RESET_ALL}: %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    return logger
