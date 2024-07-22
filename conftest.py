import pytest
from user_api import Api


@pytest.fixture(scope="session")
def api():
    return Api("https://www.sibdar-spb.ru")
