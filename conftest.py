import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="undefined language: use \"--language es}\"")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def language(request):
    language = request.config.getoption("language")

    if (language == None):
        raise pytest.UsageError("parameter --language is required")

    return language
