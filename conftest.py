import os
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.88:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~\\Downloads\\drivers"))


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(executable_path=f"{drivers}/chromedriver", options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(executable_path=f"{drivers}/geckodriver", options=options)
    elif browser_name == "opera":
        driver = webdriver.Opera()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser not supported!")

    driver.maximize_window()
    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
