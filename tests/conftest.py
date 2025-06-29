import os
import json

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from demoqa.utils import attachments


@pytest.fixture(scope="session", autouse=True)
def generate_message():
    yield
    telebot_send_message()


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


def telebot_send_message():
    os.system("allure generate allure-results --clean")
    bot_token = os.getenv("BOT_TOKEN")
    group_id = os.getenv("TELEGRAM_GROUP_ID")
    user = os.getenv("USER_NAME")
    notifications_path = os.path.dirname(os.path.dirname(__file__))
    telegram_dict = {
        "base": {
            "project": "demoqa",
            "environment": "qaguru lesson",
            "comment": user,
            "reportLink": "",
            "language": "ru",
            "allureFolder": "allure-report",
            "enableChart": True,
        },
        "telegram": {"token": bot_token, "chat": group_id, "replyTo": ""},
    }

    with open(
        os.path.join(notifications_path, "notifications", "telegram.json"),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(json.dumps(telegram_dict))

    os.system(
        'java "-DconfigFile=./notifications/telegram.json" -jar ./notifications/allure-notifications-4.9.0.jar'
    )
    with open(
        os.path.join(notifications_path, "notifications", "telegram.json"),
        "w",
        encoding="utf-8",
    ) as file:
        print(f"{file} - file clear")
