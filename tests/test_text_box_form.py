from demoqa.model.pajes.text_box_form import TextBoxPage
from tests_data.user_info import User
from selene import browser



def test_text_box():
    text_box_page = TextBoxPage(browser)
    text_box_page.open_page()
    text_box_page.fill_text_box_form()
    print()