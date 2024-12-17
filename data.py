ORDER_1 = {
    "firstName": "Lois",
    "lastName": "Lane",
    "address": "Metropolis, Daily Planet, 5",
    "metroStation": 3,
    "phone": "+7 987 355 45 35",
    "rentTime": 3,
    "deliveryDate": "2024-12-20",
    "color": [
        "BLACK"
    ]
}
ORDER_2 = {
    "firstName": "Clark",
    "lastName": "Kent",
    "address": "Smallville, Kent Farm, 5",
    "metroStation": 7,
    "phone": "+7 945 325 56 35",
    "rentTime": 1,
    "deliveryDate": "2024-12-24",
    "color": [
        "GREY", "BLACK"
    ]
}
ORDER_3 = {
    "firstName": "Jimmy",
    "lastName": "Olsen",
    "address": "Metropolis, Main St. 2",
    "metroStation": 5,
    "phone": "+7 965 327 59 30",
    "rentTime": 7,
    "deliveryDate": "2024-12-22",
}

COURIER_CREATED = {'ok': True}
SAME_LOGIN_ERROR = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
NOT_ENOUGH_DATA_FOR_REGISTRATION_ERROR = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
COURIER_NOT_FOUND_ERROR = {'code': 404, 'message': 'Учетная запись не найдена'}
NOT_ENOUGH_DATA_FOR_LOGIN_ERROR = {'code': 400, 'message': 'Недостаточно данных для входа'}
NOT_EXISTING_DATA_ERROR = [404, {'code': 404, 'message': 'Учетная запись не найдена'}]