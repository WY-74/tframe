from pytest import Parser, Config


ENV = {}


def pytest_addoption(parser: Parser):
    mygroup = parser.getgroup(name="iframe")
    mygroup.addoption("--browser", default="Chrome", help="Which browser driver to start")
    mygroup.addoption("--debugger", default=False, help="Start debug mode")
    mygroup.addoption("--headless", default=False, help="No browser visualization interface enabled")


def pytest_configure(config: Config):
    browser = config.getoption("--browser")
    debug = config.getoption("--debugger")
    headless = config.getoption("--headless")
    print(f"{browser} driver has been started")
    print(f"debug mode: {debug}")
    print(f"headless: {headless}")
    ENV["browser"] = browser
    ENV["debugger"] = debug
    ENV["headless"] = headless
