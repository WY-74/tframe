from selenium import webdriver
from env import ENV

def instantiate_driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    if ENV.CHROME_DEBUG:
        options.debugger_address = "localhost:9000"

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    return driver
