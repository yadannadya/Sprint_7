import pytest
from methods.methods import Methods
import helpers


@pytest.fixture #для регитрации
def generate_courier_and_delete():
    courier = helpers.faker_courier()
    #Methods.create_courier(body=body)
    login = courier["login"]
    password = courier["password"]
    
    yield [courier, login, password]

    id_courier = Methods.login_courier(login, password).json()["id"]
    Methods.delete_courier(id_courier)

