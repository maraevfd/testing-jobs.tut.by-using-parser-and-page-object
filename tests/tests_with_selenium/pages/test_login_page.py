

def test_login_with_invalid_data(login_page):
    login_page.open()
    login_page.enter_username('fedor1234@mail.ru')
    login_page.enter_password('1234567')
    login_page.click_enter_button()
    login_page.check_guest_could_not_enter()


def test_go_to_main_page(login_page):
    login_page.open()
    login_page.go_to_main_page()



