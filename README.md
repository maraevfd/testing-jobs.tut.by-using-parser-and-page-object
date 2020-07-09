The procedure for working with the jobs_parser:
1. Create an instance of the VacancyParser class and pass it the keyword to search for vacancies (python).
2. Parse vacancies using the parse_vacancies method.
3. Create an instance of the KeywordCounter class and pass it the instance of the VacancyParser class
and the keywords for counting (vacancy_parser_object, python, flask, linux).
4. Use count_words method to count keywords. The result is stored in the dictionary with keyword as a keys
and amount of keyword as a values.

The  directory 'tests' contains tests for the first task JobParser and the directory 'tests with selenium'.

In this model, I tried to implement the PageObject pattern.

'Tests with selenium' directory contains test files, configuration file for the tests and 'pages' directory.

The 'pages' directory contains page model files for testing. Each module describes the methods that I use during testing.
File locators.py contains some special locators for different elements on pages.
