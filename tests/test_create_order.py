import pytest
import allure
import requests
import data
from methods.order_methods import OrderMethods


@allure.title('Тесты на создание заказа')

class TestCreateOrder:
    @allure.description('Тест на создание заказа с разными входными данными')
    @pytest.mark.parametrize('order_data', [data.ORDER_1, data.ORDER_2, data.ORDER_3])
    def test_create_order(self, order_data):
        order = OrderMethods().create_order(order_data)
        assert order[0] == 201 and order[1] is not None

    @allure.description('Тест на получение списка заказов')
    def test_get_the_orders_list(self):
        orders_list = OrderMethods().get_orders_list()
        assert orders_list[0] == 200 and orders_list[1] is not None