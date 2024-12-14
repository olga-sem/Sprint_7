import allure
from methods.courier_methods import CourierMethods


@allure.title('Тесты на регистрацию курьера')

class TestCourierMethods:
    @allure.description('Тест на регистрацию курьера с валидными данными')
    def test_create_courier_with_all_fields(self, courier):
        courier_1 = CourierMethods().create_new_courier(courier)
        assert courier_1[0] == 201 and courier_1[1] == {'ok': True}

    @allure.description('Тест на регистрацию курьера с одинаковыми данными')
    def test_create_same_courier(self, courier):
        courier_1 = CourierMethods().create_courier_with_same_data(courier)
        assert courier_1[0] == 409 and courier_1[1] == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.description('Тест на регистрацию курьера без пароля')
    def test_create_courier_without_password(self):
        courier_1 = CourierMethods().create_courier_without_required_field("JohnB", "", "John")
        assert courier_1[0] == 400 and courier_1[1] == {'code': 400, 'message': 'Недостаточно данных для создания учетной запси'}