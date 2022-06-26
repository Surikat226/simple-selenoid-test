import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_ver", action="store", default="102.0")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_ver = request.config.getoption('--browser_ver')

    capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_ver,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    yield browser
    time.sleep(3)
    browser.quit()

