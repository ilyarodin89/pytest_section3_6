
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# в задании указано, что можно использовать только браузер Chrome, поэтому в параметрах только language
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    option = Options()
    option.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=option)
    yield browser
    print("\nquit browser..")
    browser.quit()






