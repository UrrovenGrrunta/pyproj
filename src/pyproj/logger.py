import logging
import colorama


colorama.init(autoreset=True)

logging.basicConfig(level=logging.INFO, format="%(message)s")


def info(message: str) -> None:
    logging.info(colorama.Fore.CYAN + message)


def success(message: str) -> None:
    logging.info(colorama.Fore.GREEN + message)


def warning(message: str) -> None:
    logging.warning(colorama.Fore.YELLOW + message)


def error(message: str) -> None:
    logging.error(colorama.Fore.RED + message)
