from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def enter_search_word(self, search_word):
        input_search_text = self.find_element(
            MainPageLocators.LOCATOR_SEARCH_FIELD)
        input_search_text.send_keys(search_word)

    def click_search_button(self):
        send_button = self.find_element(MainPageLocators.LOCATOR_SEARCH_BUTTON)
        send_button.click()

    def check_vacancies_doesnt_exist(self, search_word):
        search_result_header = self.find_element(
            MainPageLocators.LOCATOR_SEARCH_HEADER)
        assert search_result_header.text == f'По запросу «{search_word}» ничего не найдено'

    def check_vacancies_existence(self):
        vacancy_block = self.find_elements(MainPageLocators.LOCATOR_VACANCY_BLOCK)
        assert vacancy_block

    def go_to_login_page(self):
        login_button = self.find_elements(MainPageLocators.LOCATOR_LOGIN_BUTTON)[-1]
        login_button.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def create_advanced_search(self):
        advanced_search_button = self.find_element(
            MainPageLocators.LOCATOR_ADVANCED_SEARCH_BUTTON)
        advanced_search_button.click()
