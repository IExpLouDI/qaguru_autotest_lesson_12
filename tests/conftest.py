import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demoqa.utils import attachments
from tests_data.user_info import User


@pytest.fixture(scope='function')
def setup_browser():

    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVideo": True
        }
    }

    options.page_load_strategy = "eager"
    options.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser
    attachments.add_html(browser)
    attachments.add_logs(browser)
    attachments.add_screenshot(browser)
    browser.close()


@pytest.mark.parametrize('fio', 'mail', 'curr_address', 'per_address',
                         ())
@pytest.fixture(scope='function')
def get_user(fio, mail, curr_address, per_address):
    return User(full_name=fio, email=mail, current_address=curr_address, permanent_address=per_address)


@pytest.fixture()
def valid_info(get_user):

    return ['Name:', 'Test',
            'mail:', 'sss@example.com',
            'Current Address:', 'tttsss',
            'Permananet Address:', 'sssss']