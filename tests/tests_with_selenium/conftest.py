import pytest
from selenium import webdriver
from .pages.main_page import MainPage


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# @pytest.fixture(scope="module")
# def main_page():
#     link = 'https://jobs.tut.by/'
#     main_page = MainPage(browser, link)
#     yield main_page

