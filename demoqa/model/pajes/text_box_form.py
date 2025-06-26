import allure
from selene import be, have

from tests_data.user_info import User


class TextBoxPage:
    def __init__(self, setup):
        self.browser = setup

    @allure.step('Открываем форму text-box')
    def open_page(self):
        self.browser.open('https://demoqa.com/text-box')
        self.browser.driver.execute_script("$('footer').remove()")
        self.browser.driver.execute_script("$('#fixedban').remove()")
        return self


    def fill_full_name(self, value):
        self.browser.element('#userName').type(value)
        return self

    def fill_email(self, value):
        self.browser.element('#userEmail').type(value)
        return self

    def fill_current_address(self,value):
        self.browser.element('#currentAddress').type(value)
        return self

    def fill_permanent_address(self,value):
        self.browser.element('#permanentAddress').type(value)
        return self

    def press_submit(self):
        self.browser.element('#submit').click()
        return self

    def should_be_form_info(self, values:list):
        self.browser.element('#output').all('p').should(have.exact_text(values))

    def fill_text_box_form(self,user:User):

        with allure.step('Заполняем ФИО'):
            self.fill_full_name(user.full_name)

        with allure.step('Заполняем email {user.email}'):
            self.fill_email(user.email)

        with allure.step('Заполняем фактический адрес {user.current_address}'):
            self.fill_current_address(user.current_address)

        with allure.step('Заполняем адрес прописки {user.permanent_address}'):
            self.fill_permanent_address(user.permanent_address)

        with allure.step('Публикуем форму submit'):
            self.press_submit()
