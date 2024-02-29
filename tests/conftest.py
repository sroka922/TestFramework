import pytest
from selenium import webdriver
from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("no default browser. set to chrome as a default")
        driver = webdriver.Chrome()
    driver.maximize_window()
    url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
