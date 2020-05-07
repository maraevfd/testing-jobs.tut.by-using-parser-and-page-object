from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR,
                            'input[data-qa=search-input]')
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR,
                             'span.supernova-search-submit-text')
    LOCATOR_SEARCH_HEADER = (By.CSS_SELECTOR,
                             'h1.bloko-header-1')
    LOCATOR_VACANCY_BLOCK = (By.CSS_SELECTOR,
                             'h1.bloko-header-1')
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR,
                            'a[data-qa="login"]')
    LOCATOR_ADVANCED_SEARCH_BUTTON = (By.CSS_SELECTOR,
                                      'span.bloko-icon_highlighted-default')
