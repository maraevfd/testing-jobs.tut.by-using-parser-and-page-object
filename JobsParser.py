from bs4 import BeautifulSoup
from random import choice
import requests
import re

# Basic url for creating an HTTPS request for Jobs.Tut.By website
URL = 'https://jobs.tut.by/search/vacancy'

# The parameter used in the header of the HTTPS request to bypass
# the blocking of connection to the site using the request library
DESKTOP_AGENTS = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 '
    '(KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ']

# Dictionary for user-agent parameter transfer in HTTP request
HEADERS = {'User-Agent': choice(DESKTOP_AGENTS)}


class VacancyParser:
    """The parser is designed to parse all links to vacancies on the
    Jobs.Tut.By website using a keyword for search. Using this class
    is only relevant for the website.
    """

    def __init__(self, search_word=None):
        """Constructor.

        :param search_word: A string object which is used for
        the search query.
        """

        self.search_word = search_word
        self.links = []

    def set_search_word(self, new_search_word):
        """The method allows you to change the initial search keyword
        """

        self.links.clear()
        self.search_word = new_search_word
        print("Search word changed successfully", self.search_word)

    def parse_vacancies(self):
        """The method creates a request for searching and parsing all
        links to vacancies
        """

        self.links.clear()
        params = {'L_is_autosearch': 'false',
                  'area': 1002,
                  'clusters': 'true',
                  'enable_snippets': 'true',
                  'salary': None,
                  'st': 'searchVacancy',
                  'text': self.search_word,
                  'page': 0}

        vacancy_divs = True
        while vacancy_divs:
            response = requests.get(URL, headers=HEADERS, params=params)
            soup = BeautifulSoup(response.content, 'html.parser')
            vacancy_divs = soup.find_all('div', class_='vacancy-serp-item')
            self.links += [tag['href'] for tag in
                           soup.find_all('a', class_='HH-LinkModifier')]
            params['page'] += 1
        print(len(self.links))
        return self.links

    def __str__(self):
        return 'Search word is {}'.format(self.search_word)


class KeywordCounter:
    """The class is designed to calculate the given keywords in the vacancies
    that the VacancyParser object contains.
    """

    def __init__(self, vacancy_parser: VacancyParser, *keywords):
        """Constructor.

        :param vacancy_parser: Object VacancyParser which contains links to
        vacancies and other information ot create HTTP request.

        :param keywords: A set object which contains keywords for counting
        them among the contents of a given link.
        """

        self.vacancy_parser = vacancy_parser
        self.keywords = keywords

    def set_keywords(self, *new_keywords):
        """The method allows you to change the initial keywords to count
        """

        self.keywords = new_keywords
        print("Keywords changed successfully", self.keywords)

    @staticmethod
    def _get_vacancy_content(links):
        """A generator that takes a sequence of vacancies references
        as strings and returns the contents of each vacancy.
        """

        for link in links:
            response = requests.get(link, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.find_all('div', class_='vacancy-description')
            yield content

    def count_words(self):
        """Contents of all tags are concatenated into a single string and
         all keywords are counted. The method returns a dictionary with
         keyword as a keys and amount of keyword as a values.
         """

        joined_text = ''.join(tag.text for content in
                              self._get_vacancy_content(self.vacancy_parser.links)
                              for tag in content)

        result = {}
        for pattern in self.keywords:
            n_words = len(re.findall(pattern,
                                     joined_text,
                                     flags=re.IGNORECASE))
            result[pattern] = result.get(pattern, 0) + n_words

        return result

    def __str__(self):
        return 'Keywords are {}'.format(self.keywords)


if __name__ == '__main__':
    python_vacancies = VacancyParser('python')
    python_vacancies.parse_vacancies()
    keywords_set = KeywordCounter(python_vacancies, 'python', 'linux', 'flask')
    result_dict = keywords_set.count_words()
    for word in result_dict:
        print('The word', word, 'has been found', result_dict[word], 'times')
