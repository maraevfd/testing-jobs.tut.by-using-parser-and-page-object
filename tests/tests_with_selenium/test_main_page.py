from tests.tests_with_selenium.pages.main_page import MainPage
import pytest


@pytest.mark.parametrize('search_word', ['asdhfapsdhgasf',
                                         'shotgun',
                                         'somelongword'])
def test_search_by_wrong_word(browser, search_word):
    link = 'https://jobs.tut.by/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.enter_search_word(search_word)
    main_page.click_search_button()
    main_page.check_vacancies_doesnt_exist(search_word)


@pytest.mark.parametrize('search_word', ['python',
                                         'java',
                                         'devops'])
def test_search_by_correct_word(browser, search_word):
    link = 'https://jobs.tut.by/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.enter_search_word(search_word)
    main_page.click_search_button()
    main_page.check_vacancies_existence()


def test_go_to_login_page(browser):
    link = 'https://jobs.tut.by/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()


def test_go_to_advanced_search(browser):
    link = 'https://jobs.tut.by/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.create_advanced_search()
