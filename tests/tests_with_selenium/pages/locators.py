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


class LoginPageLocators:
    LOCATOR_USERNAME_FIELD = (By.CSS_SELECTOR,
                              'input[name="username"]')
    LOCATOR_PASSWORD_FIELD = (By.CSS_SELECTOR,
                              'input[name="password"]')
    LOCATOR_ENTER_BUTTON = (By.CSS_SELECTOR,
                            'input[data-qa="account-login-submit"]')
    LOCATOR_ERROR_MESSAGE = (By.CSS_SELECTOR,
                             'div[data-qa="account-flash-error"]')
    LOCATOR_MAIN_PAGE = (By.CSS_SELECTOR,
                         'span.supernova-logo_jobs-tut-by')
