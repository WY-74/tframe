import logging


LOG_PATH = "/tmp/records.log"


def main():
    logger = logging.getLogger("tframe")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s - %(asctime)s] %(message)s", datefmt="%m/%d/%Y-%I:%M:%S-%p")

    file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def clear_log():
    with open(LOG_PATH, "r+") as f:
        f.truncate(0)


class Logger:
    def __init__(self, clear: bool = False):
        self.logger = main()
        if clear:
            clear_log()

    def info(self, message: str):
        self.logger.info(f"\n\t{message}")

    def warning(self, message: str):
        self.logger.warning(f"\n\t{message}")
        raise Exception(message)
