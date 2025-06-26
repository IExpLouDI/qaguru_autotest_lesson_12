import allure
import pytest
from allure_commons.types import Severity

from demoqa.model.pajes.text_box_form import TextBoxPage
from demoqa.utils.functions import valid_info
from tests_data.person_data import test_cases
from tests_data.user_info import User


@allure.id("01_test_text_box")
@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "vssuchkov")
@allure.feature("Заполнение формы пользователя")
@allure.story("Формы регистрации")
@allure.link("https://demoqa.com/text-box", name="Testing url")
@pytest.mark.parametrize("fio, mail, curr_address, per_address", test_cases)
def test_text_box(setup_browser, fio, mail, curr_address, per_address):
    user = User(fio, mail, curr_address, per_address)
    valid_user_info = valid_info(user)

    text_box_page = TextBoxPage(setup_browser)
    text_box_page.open_page()
    text_box_page.fill_text_box_form(user)
    text_box_page.should_be_form_info(valid_user_info)
