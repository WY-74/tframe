import time
import yaml
from typing import Callable


def exception_capture(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            driver = args[0].driver

            timestamp = int(time.time())
            driver.save_screenshot(f"log/screenshot/{func.__name__}_{timestamp}.png")
            with open(f"log/page_source/{func.__name__}_{timestamp}.html", "w") as f:
                f.write(driver.page_source)
            # TODO: 后续需要完善将截图和page source添加到allure报告中
            raise Exception

    return inner


def save_cookies(func: Callable):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        driver = args[0].driver
        cookies = driver.get_cookies()
        with open(f"cookies.yaml", "w") as f:
            yaml.safe_dump(cookies, f)

    return inner


def load_cookies(func: Callable):
    def inner(*args, **kwargs):
        driver = args[0].driver
        cookies = yaml.safe_load(open("cookies.yaml"))
        for c in cookies:
            driver.add_cookie(c)
        func(*args, **kwargs)

    return inner
