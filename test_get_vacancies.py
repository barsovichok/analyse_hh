

def test_hh_url(hh_url):
    assert 'hh' in hh_url


def test_response_vacancies(response_vacancies):
    assert 'items' in response_vacancies


def test_response_vacancies_id(response_vacancies):
    assert 'id' in response_vacancies.get('items')
