import pytest
import requests
import helpers
import urls
from methods.login_methods import LoginMethods


@pytest.fixture(scope='function')
def create_and_delete_courier():
    payload = helpers.create_new_courier_and_return_login_password()
    yield payload
    id_courier = LoginMethods().courier_login(payload)[1]
    requests.delete(f'{urls.BASE_URL}{urls.COURIER_URL}/{id_courier}')

