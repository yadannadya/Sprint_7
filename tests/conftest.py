import pytest
from methods.methods import Methods
import helpers
from data import Person
import requests

@pytest.fixture
def generate_courier_and_delete():
    courier = helpers.faker_courier()
    login = courier["login"]
    password = courier["password"]
    
    yield [courier, login, password]

    id_courier = Methods.login_courier(login, password).json()["id"]
    Methods.delete_courier(id_courier)

@pytest.fixture
def create_order_and_delete():
    body_response = Methods.create_order(Person.black).json()
    track = body_response["track"]
    id_order = Methods.get_order_by_track(track).json()["order"]["id"]

    yield [track, id_order]
    Methods.delete_order(track)
    


@pytest.fixture
def create_courier_and_return_id():
    courier = helpers.faker_courier()
    Methods.create_courier(courier)
    id_courier = Methods.login_courier(courier["login"], courier["password"]).json()["id"]
   
    yield id_courier
    response = Methods.login_courier(courier["login"], courier["password"])
    if response.status_code == 200:
        Methods.delete_courier(id_courier)
    
    