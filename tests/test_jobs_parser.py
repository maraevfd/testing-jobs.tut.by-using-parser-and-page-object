import jobs_parser
import requests
import pytest


@pytest.fixture(scope='function')
def vacancy_parser():
    vacancy_parser = jobs_parser.VacancyParser('python')
    yield vacancy_parser
    del vacancy_parser


class TestVacancyParser:

    def test_connection_to_the_site(self):
        response = requests.get(jobs_parser.URL, headers=jobs_parser.HEADERS)
        assert response.status_code == 200

    def test_change_keyword_to_search(self, vacancy_parser):
        vacancy_parser.set_search_word('java')
        assert vacancy_parser.search_word == 'java'

    def test_parse_vacancies(self, vacancy_parser):
        vacancy_parser.set_search_word('java')
        vacancy_parser.parse_vacancies()
        assert vacancy_parser.links

    def test_search_by_wrong_keyword(self, vacancy_parser):
        vacancy_parser.set_search_word('shotgun')
        vacancy_parser.parse_vacancies()
        assert not vacancy_parser.links

    def test_parsed_vacancies_is_available(self, vacancy_parser):
        vacancy_parser.set_search_word('python')
        vacancy_parser.parse_vacancies()
        for link in vacancy_parser.links:
            response = requests.get(link, headers=jobs_parser.HEADERS)
            assert response.status_code == 200







