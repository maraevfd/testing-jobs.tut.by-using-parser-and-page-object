import jobs_parser
import pytest


@pytest.fixture(scope="function")
def keyword_counter():
    vacancy_parser = jobs_parser.VacancyParser('python')
    vacancy_parser.parse_vacancies()
    keyword_counter = jobs_parser.KeywordCounter(vacancy_parser,
                                                 'python',
                                                 'flask',
                                                 'linux')
    yield keyword_counter
    del keyword_counter
    del vacancy_parser


class TestKeywordCounter:

    def test_change_keyword_to_search(self, keyword_counter):
        keyword_counter.set_keywords('docker', 'django')
        assert keyword_counter.keywords == ('docker', 'django')

    def test_count_given_words_in_vacancies(self, keyword_counter):
        keyword_counter.set_keywords('python', 'linux', 'flask')
        result_dict = keyword_counter.count_words()
        for word in result_dict:
            assert result_dict[word] > 0

    def test_count_wrong_words(self, keyword_counter):
        keyword_counter.set_keywords('shotgun', 'killer', 'girlfriend')
        result_dict = keyword_counter.count_words()
        for word in result_dict:
            assert result_dict[word] == 0

    def test_count_empty_string(self, keyword_counter):
        keyword_counter.set_keywords()
        result_dict = keyword_counter.count_words()
        assert not result_dict
