from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en e.t.d.")
    
    # По умолчанию работает только chrome.
@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language")
    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    browser.quit()

