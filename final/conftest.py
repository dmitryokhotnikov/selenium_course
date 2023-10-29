import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, eng or other")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f"\nstart browser for test...")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language parameter is incorrect")
    yield browser
    print("\nquit browser..")
    browser.quit()
