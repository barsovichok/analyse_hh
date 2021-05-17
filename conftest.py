import pytest
import get_vacancies


@pytest.fixture
def hh_url(url=get_vacancies.api_url):
    return url


@pytest.fixture
def response_vacancies(response_vacancies=get_vacancies.response_vacancies):
    return response_vacancies
