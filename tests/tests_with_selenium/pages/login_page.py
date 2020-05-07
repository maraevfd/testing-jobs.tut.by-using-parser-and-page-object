from .base_page import BasePage


class LoginPage(BasePage):

    def check_only_in(self, email):
        input_email_field = self.browser.find_element_by_css_selector('input[name="username"]')
        input_email_field.send_keys(email)

    def enter_password(self, password):
        input_email_field = self.browser.find_element_by_css_selector('input[name="password"]')
        input_email_field.send_keys(password)

    def click_enter_button(self):
        enter_button = self.browser.find_element_by_css_selector('input[data-qa="account-login-submit"]')
        enter_button.click()

    def check_guest_could_not_enter(self):
        error_message = self.browser.find_element_by_css_selector('div.[data-qa="account-flash-error"]')
        assert error_message.text == 'Неправильные данные для входа. Пожалуйста, попробуйте снова.'
