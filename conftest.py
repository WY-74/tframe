from pytest import Parser, Config


ENV = {}


def pytest_addoption(parser: Parser):
    mygroup = parser.getgroup(name="iframe")
    mygroup.addoption("--browser", default="Chrome", help="Which browser driver to start")
    mygroup.addoption("--debugger", default=False, help="Whether to enable debug mode")


def pytest_configure(config: Config):
    browser = config.getoption("--browser")
    debug = config.getoption("--debugger")
    print(f"{browser} driver has been started")
    print(f"debug mode: {debug}")
    ENV["browser"] = browser
    ENV["debugger"] = debug
