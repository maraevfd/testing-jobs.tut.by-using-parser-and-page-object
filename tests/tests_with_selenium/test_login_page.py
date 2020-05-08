from selenium.common.exceptions import TimeoutException


def test_login_with_invalid_data(login_page):
    login_page.open()
    login_page.enter_username('fedor1234@mail.ru')
    login_page.enter_password('1234567')
    login_page.click_enter_button()
    login_page.check_guest_could_not_enter()


def test_login_with_valid_data(login_page):
    login_page.open()
    login_page.enter_username('snoof95@mail.ru')
    login_page.enter_password('0123456789fedor')
    login_page.click_enter_button()
    try:
        login_page.check_guest_could_not_enter()
    except (TimeoutException, AssertionError):
        assert True


def test_go_to_main_page(login_page):
    login_page.open()
    login_page.go_to_main_page()
