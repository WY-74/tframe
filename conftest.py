from pytest import Parser, Config


ENV = {}


def pytest_addoption(parser: Parser):
    mygroup = parser.getgroup(name="iframe")
    mygroup.addoption("--browser", default="Chrome", help="Which browser driver to start")
    mygroup.addoption("--debugger", default=False, help="Start debug mode")
    mygroup.addoption("--headless", default=False, help="No browser visualization interface enabled")
    mygroup.addoption("--remote", default=False, help="Distributed execution of programs")


def pytest_configure(config: Config):
    browser = config.getoption("--browser")
    debug = config.getoption("--debugger")
    headless = config.getoption("--headless")
    remote = config.getoption("--remote")
    print(f"browser: {browser}")
    print(f"debug mode: {debug}")
    print(f"headless: {headless}")
    print(f"remote: {remote}")
    ENV["browser"] = browser
    ENV["debugger"] = debug
    ENV["headless"] = headless
    ENV["remote"] = remote
