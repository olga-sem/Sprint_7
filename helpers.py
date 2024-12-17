import string
import random


def create_new_courier_and_return_login_password():
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload