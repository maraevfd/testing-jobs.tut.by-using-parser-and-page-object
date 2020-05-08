import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.fixture(scope="module")
def main_page():
    browser = webdriver.Chrome()
    link = 'https://jobs.tut.by/'
    main_page = MainPage(browser, link)
    yield main_page
    browser.quit()


@pytest.fixture(scope="function")
def login_page():
    browser = webdriver.Chrome()
    link = 'https://jobs.tut.by/account/login?backurl=%2F'
    login_page = LoginPage(browser, link)
    yield login_page
    browser.quit()
