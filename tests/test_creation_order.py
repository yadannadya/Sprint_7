import pytest
from methods.methods import Methods
from data import Person
import allure
        
class TestCreationOrder:

    @allure.title('Успешное создание заказа самоката') 
    @pytest.mark.parametrize('info', Person.lst1)
    def test_create_order_success(self, info):
        response = Methods.create_order(body=info)
        assert response.status_code == 201
        assert type(response.json()["track"]) == int
        Methods.delete_order(response.json()["track"])