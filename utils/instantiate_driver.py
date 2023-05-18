from selenium import webdriver
from conftest import ENV
from utils.capabilities import CAPABILITIES


def instantiate_driver():
    browser = ENV["browser"]

    if not ENV["remote"]:
        options = getattr(webdriver, f"{browser}Options")()
        options.page_load_strategy = 'eager'
        if ENV["headless"]:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        if ENV["debugger"]:
            options.debugger_address = "localhost:9000"

        driver = getattr(webdriver, ENV["browser"])(options=options)
        driver.maximize_window()
        driver.implicitly_wait(3)

    hogwarts_grid_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"  # 这是一个暂时的节点终端
    capabilities = CAPABILITIES
    driver = webdriver.Remote(command_executor=hogwarts_grid_url, desired_capabilities=capabilities)

    return driver
