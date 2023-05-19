from selenium import webdriver
from playwright.sync_api import sync_playwright

from conftest import ENV
from utils.capabilities import CAPABILITIES


def instantiate_driver():
    headless = ENV["headless"]
    if ENV["suite"] == "selenium":
        if not ENV["remote"]:
            options = getattr(webdriver, f"{ENV['web']}Options")()
            options.page_load_strategy = 'eager'
            if headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
            if ENV["debugger"]:
                options.debugger_address = "localhost:9000"
            web = getattr(webdriver, ENV['web'])(options=options)
            web.maximize_window()
            web.implicitly_wait(3)
            return web
        hogwarts_grid_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"  # 这是一个暂时的节点终端
        capabilities = CAPABILITIES
        web = webdriver.Remote(command_executor=hogwarts_grid_url, desired_capabilities=capabilities)
    elif ENV["suite"] == "playwright":
        web = sync_playwright().start().chromium.launch(headless=bool(headless)).new_page()
    else:
        raise Exception("[Err]: Please set up 'selenium' or 'playwriht' via --suite")

    return web
