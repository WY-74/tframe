from selenium import webdriver
from conftest import ENV


def instantiate_driver():
    browser = ENV["browser"]
    options = getattr(webdriver, f"{browser}Options")()
    options.page_load_strategy = 'eager'

    if ENV["debugger"]:
        options.debugger_address = "localhost:9000"

    driver = getattr(webdriver, ENV["browser"])(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    return driver
