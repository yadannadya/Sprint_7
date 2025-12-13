import requests
from methods.methods import Methods
import pytest
import allure

        
class TestListOrder:

    @allure.title('Успешное получение списка заказов самокатов')
    def test_get_list_order_success(self):
        response = Methods.get_list_order()
        assert response.status_code == 200
        assert type(response.json()["orders"]) is list