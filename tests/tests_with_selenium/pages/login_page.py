from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_username(self, email):
        input_email_field = self.find_element(LoginPageLocators.LOCATOR_USERNAME_FIELD)
        input_email_field.send_keys(email)

    def enter_password(self, password):
        input_email_field = self.find_element(LoginPageLocators.LOCATOR_PASSWORD_FIELD)
        input_email_field.send_keys(password)

    def click_enter_button(self):
        enter_button = self.find_element(LoginPageLocators.LOCATOR_ENTER_BUTTON)
        enter_button.click()

    def check_guest_could_not_enter(self):
        error_message = self.find_element(LoginPageLocators.LOCATOR_ERROR_MESSAGE)
        assert error_message.text == 'Неправильные данные для входа. Пожалуйста, попробуйте снова.'

    def go_to_main_page(self):
        main_page_button = self.find_element(LoginPageLocators.LOCATOR_MAIN_PAGE)
        main_page_button.click()
