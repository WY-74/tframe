from pytest import Parser, Config


ENV = {}


def pytest_addoption(parser: Parser):
    mygroup = parser.getgroup(name="iframe")
    mygroup.addoption("--suite", help="You can choose 'selenium' or 'playwright' to help you get the job done")
    mygroup.addoption("--web", default="Chrome", help="Which browser driver to start")
    mygroup.addoption("--headless", default=False, help="No browser visualization interface enabled")
    mygroup.addoption("--debugger", default=False, help="[Only Selenium] [Only Chrome] Start debug mode")
    mygroup.addoption("--remote", default=False, help="[Only Selenium] Distributed execution of programs")


def pytest_configure(config: Config):
    suite = config.getoption("--suite")
    web = config.getoption("--web")
    headless = config.getoption("--headless")
    debug = config.getoption("--debugger")
    remote = config.getoption("--remote")
    print(f"{suite} -> {web}")
    print(f"headless: {headless}")
    print(f"debug mode: {debug}")
    print(f"remote: {remote}")
    ENV["suite"] = suite
    ENV["web"] = web
    ENV["headless"] = headless
    ENV["debugger"] = debug
    ENV["remote"] = remote
