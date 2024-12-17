import allure
from data import COURIER_CREATED, SAME_LOGIN_ERROR, NOT_ENOUGH_DATA_FOR_REGISTRATION_ERROR
from methods.courier_methods import CourierMethods


class TestCourierMethods:
    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем создание курьера с валидными данными')
    def test_create_courier_with_all_fields(self, create_and_delete_courier):
        courier_1 = CourierMethods().create_new_courier(create_and_delete_courier)
        assert courier_1[0] == 201 and courier_1[1] == COURIER_CREATED

    @allure.title('Тест на регистрацию курьера с одинаковыми данными')
    @allure.description('Проверяем невозможность создания курьеров с одинаковыми данными')
    def test_create_same_courier(self, create_and_delete_courier):
        CourierMethods().create_new_courier(create_and_delete_courier)
        courier_2 = CourierMethods().create_new_courier(create_and_delete_courier)
        assert courier_2[0] == 409 and courier_2[1] == SAME_LOGIN_ERROR

    @allure.title('Тест на регистрацию курьера без пароля')
    @allure.description('Проверяем невозиожность регистрации курьера без заполнения обязательного поля Пароль')
    def test_create_courier_without_password(self, create_and_delete_courier):
        payload = {
                   "login": create_and_delete_courier["login"],
                   "password": "",
                   "firstName": create_and_delete_courier["firstName"]
                  }
        courier_1 = CourierMethods().create_new_courier(payload)
        assert courier_1[0] == 400 and courier_1[1] == NOT_ENOUGH_DATA_FOR_REGISTRATION_ERROR