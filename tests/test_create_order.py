import pytest
import allure
import data
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Тест на создание заказа с разными входными данными')
    @allure.description('Проверяем создание заказа с разными входными данными для поля Цвет: один цвет, два цвета, без указания цвета')
    @pytest.mark.parametrize('order_data', [data.ORDER_1, data.ORDER_2, data.ORDER_3])
    def test_create_order(self, order_data):
        order = OrderMethods().create_order(order_data)
        assert order[0] == 201 and order[1] is not None

    @allure.title('Тест на получение списка заказов')
    @allure.description('Проверяем получение списка заказов')
    def test_get_the_orders_list(self):
        orders_list = OrderMethods().get_orders_list()
        assert orders_list[0] == 200 and "orders" in orders_list[1]