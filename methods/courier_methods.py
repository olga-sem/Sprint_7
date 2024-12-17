import requests
import allure
import urls


class CourierMethods:

    @allure.step('Метод для создания курьера')
    def create_new_courier(self, payload):
        response = requests.post(f'{urls.BASE_URL}{urls.COURIER_URL}', data = payload)
        return [response.status_code, response.json()]



