import requests
import allure

import helpers
import urls



@allure.title('Методы для работы с курьерами')
class CourierMethods:

    @allure.step('Метод для создания курьера')
    def create_new_courier(self, payload):
        response = requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data = payload)
        return [response.status_code, response.json()]

    @allure.step('Метод для создания курьера с одинаковыми данными')
    def create_courier_with_same_data(self, payload):
        requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data=payload)
        res = requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data = payload)
        return [res.status_code, res.json()]

    @allure.step('Метод для создания курьера без пароля')
    def create_courier_without_required_field(self, login, password, first_name):
        user_data = {
                    "login": login,
                    "password": password,
                    "FirstName": first_name
                    }
        response = requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data=user_data)
        return [response.status_code, response.json()]

