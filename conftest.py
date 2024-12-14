import pytest
import requests
import helpers
import urls


@pytest.fixture()
def courier():
    payload = helpers.create_new_courier_and_return_login_password()
    yield payload
    login = requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data=payload)
    id_courier = login.json()["id"]
    requests.delete(f'{urls.BASE_URL}{urls.COURIER_URL}' + str(id_courier))