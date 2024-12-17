import allure
from data import COURIER_NOT_FOUND_ERROR, NOT_ENOUGH_DATA_FOR_LOGIN_ERROR, NOT_EXISTING_DATA_ERROR
from methods.login_methods import LoginMethods


class TestLogin:
    @allure.title('Тест на авторизацию курьера с валидными данными')
    @allure.description('Проверяем авторизацию курьера с валидными данными')
    def test_login_with_all_fields(self, create_and_delete_courier):
        courier_1 = LoginMethods().courier_login(create_and_delete_courier)
        assert courier_1[0] == 200 and str(courier_1[1]) is not None

    @allure.title('Тест на авторизацию курьера с неверным паролем')
    @allure.description('Проверяем невозможность авторизоваться с неверным паролем')
    def test_login_with_wrong_password(self, create_and_delete_courier):
        courier_1 = LoginMethods().login_with_wrong_password("123456")
        assert courier_1[0] == 404 and courier_1[1] == COURIER_NOT_FOUND_ERROR

    @allure.title('Тест на авторизацию курьера без пароля')
    @allure.description('Проверяем невозможность авторизоваться без заполнения обязательного поля Пароль')
    def test_login_without_password(self, create_and_delete_courier):
        courier_1 = LoginMethods().login_without_password()
        assert courier_1[0] == 400 and courier_1[1] == NOT_ENOUGH_DATA_FOR_LOGIN_ERROR

    @allure.title('Тест на авторизацию курьера с несуществующими данными')
    @allure.description('Проверяем невозможность авторизоваться в системе с незарегистрированными данными')
    def test_login_with_not_existing_data(self):
        courier_2 = LoginMethods().login_with_not_existing_data("BradS", "123456")
        assert courier_2 == NOT_EXISTING_DATA_ERROR