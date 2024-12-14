import allure
from methods.login_methods import LoginMethods


@allure.title('Тесты на авторизацию курьера')

class TestLogin:
    @allure.description('Тест на авторизацию курьера с валидными данными')
    def test_login_with_all_fields(self, courier):
        courier_1 = LoginMethods().courier_login(courier)
        assert courier_1[0] == 200 and courier_1[1] is not None

    @allure.description('Тест на авторизацию курьера с неверным паролем')
    def test_login_with_wrong_password(self, courier):
        courier_1 = LoginMethods().login_with_wrong_password("123456")
        assert courier_1[0] == 404 and courier_1[1] == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.description('Тест на авторизацию курьера без пароля')
    def test_login_without_password(self, courier):
        courier_1 = LoginMethods().login_without_password()
        assert courier_1[0] == 400 and courier_1[1] == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.description('Тест на авторизацию курьера с несуществующими данными')
    def test_login_with_not_existing_data(self):
        courier_2 = LoginMethods().login_with_not_existing_data("BradS", "123456")
        assert courier_2 == [404, {'code': 404, 'message': 'Учетная запись не найдена'}]