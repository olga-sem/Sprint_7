import requests
import allure

import helpers
import urls


@allure.title('Методы для работы с авторизацией курьеров')
class LoginMethods:

    @allure.step('Метод для авторизации курьера')
    def courier_login(self, payload):
        requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data=payload)
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_URL}', data = payload)
        return [response.status_code, response.json()]

    @allure.step('Метод для авторизации курьера с неправильным паролем')
    def login_with_wrong_password(self, password):
        user_data = helpers.create_new_courier_and_return_login_password()
        new_data = {
                    "login": user_data["login"],
                    "password": password
                   }
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_URL}', data = new_data)
        return [response.status_code, response.json()]

    @allure.step('Метод для авторизации курьера без пароля')
    def login_without_password(self):
        user_data = helpers.create_new_courier_and_return_login_password()
        new_data = {
            "login": user_data["login"],
            "password": ""
        }
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_URL}', data=new_data)
        return [response.status_code, response.json()]

    @allure.step('Метод для авторизации курьера c несуществующими данными')
    def login_with_not_existing_data(self, login, password):
        payload = {
                   "login": login,
                   "password": password
        }
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_URL}', data=payload)
        return [response.status_code, response.json()]


