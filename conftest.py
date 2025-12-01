import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.close()
    browser.quit()
