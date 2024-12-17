import requests
import json
import allure
import urls


class OrderMethods:

    @allure.step('Метод для создания заказа')
    def create_order(self, order_data):
        payload = order_data
        json_data = json.dumps(payload)
        response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}', data = json_data)
        return [response.status_code, response.json()['track']]

    @allure.step('Метод для получения списка заказов')
    def get_orders_list(self):
        response = requests.get(f'{urls.BASE_URL}{urls.ORDER_URL}')
        return [response.status_code, response.text]