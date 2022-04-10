from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose --language: ru or es")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    if language_name == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        driver = webdriver.Chrome(options=options)
    elif language_name == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        driver = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be 'ru' or 'es'")
    yield driver
    print("\nquit browser..")
    driver.quit()
