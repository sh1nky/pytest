import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="undefined language: use \"--language es}\"")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
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
