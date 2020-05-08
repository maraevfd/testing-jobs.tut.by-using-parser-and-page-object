import pytest


@pytest.mark.parametrize('search_word', ['asdhfapsdhgasf',
                                         'shotgun',
                                         'somelongword'])
def test_search_by_wrong_word(main_page, search_word):
    main_page.open()
    main_page.enter_search_word(search_word)
    main_page.click_search_button()
    main_page.check_vacancies_doesnt_exist(search_word)


@pytest.mark.parametrize('search_word', ['python',
                                         'java',
                                         'devops'])
def test_search_by_correct_word(main_page, search_word):
    main_page.open()
    main_page.enter_search_word(search_word)
    main_page.click_search_button()
    main_page.check_vacancies_existence()


def test_go_to_login_page(main_page):
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.check_current_url('https://jobs.tut.by/account/login?backurl=%2F')


def test_go_to_advanced_search(main_page):
    main_page.open()
    main_page.go_to_advanced_search()
    main_page.check_current_url('https://jobs.tut.by/search/vacancy/advanced')
