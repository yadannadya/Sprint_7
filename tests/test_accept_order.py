import requests
import pytest
from data import Person
from methods.methods import Methods
import allure

class TestAcceptOrders:

   @allure.title('Успешное принятие заказа по id курьера')
   def test_accept_orders_success(self, create_courier_and_return_id,  create_order_and_delete):
      response = Methods.accept_orders(create_order_and_delete[1], create_courier_and_return_id)
      assert response.status_code == 200
      assert response.json() == {"ok": True }

   @allure.title('Ошибка 400 на принятие заказа без id заказа или курьера')
   @pytest.mark.parametrize('id_order, id_courier', Person.invalid_accept)
   def test_accept_orders_without_id(self, id_order, id_courier):
      response = Methods.accept_orders(id_order, id_courier)
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для поиска" 

   @allure.title('Ошибка 404 на принятие заказа с неверным id заказа')
   def test_accept_orders_with_invalid_id(self):
      response = Methods.accept_orders("1234567890", "2345")
      assert response.status_code == 404
      assert response.json()["message"] == "Заказа с таким id не существует"

   @allure.title('Ошибка 404 на принятие заказа с неверным id курьера')
   def test_accept_orders_with_invalid_courierId(self):
      response = Methods.accept_orders("1234", "1234567890")
      assert response.status_code == 404
      assert response.json()["message"] == "Курьера с таким id не существует"


   @allure.title('Нельзя повторно принять заказ')
   def test_accept_orders_with_repeat_id(self, create_courier_and_return_id,  create_order_and_delete):
      Methods.accept_orders(create_order_and_delete[1], create_courier_and_return_id)
      response = Methods.accept_orders(create_order_and_delete[1], create_courier_and_return_id)
      assert response.status_code == 409
      assert response.json()["message"] == "Этот заказ уже в работе"