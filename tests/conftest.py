import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from demoqa.utils import attachments


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser():

    login = os.getenv("SELENOID_LOGIN")
    passw = os.getenv("SELENOID_PASSWORD")
    host = os.getenv("SELENOID_HOST")

    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True, "enableLog": True},
    }

    options.page_load_strategy = "eager"
    options.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{passw}@{host}",
        options=options,
    )

    browser.config.driver = driver

    yield browser
    attachments.add_html(browser)
    attachments.add_logs(browser)
    attachments.add_screenshot(browser)
    attachments.add_video(browser)
    browser.close()
