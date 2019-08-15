import pytest


@pytest.fixture(scope='session')
def api_client():
    base_url = 'https://api.openbrewerydb.org'
    return base_url
