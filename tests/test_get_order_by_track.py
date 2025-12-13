import pytest
from methods.methods import Methods
from data import Person
import allure


class TestOrders:

   @allure.title('Успешное получение заказа по его номеру')
   def test_get_order_by_track_success(self, create_order_and_delete):
      response = Methods.get_order_by_track(create_order_and_delete[0])
      assert response.status_code == 200
      assert type(response.json()["order"]) == dict

   @allure.title('Нельзя получить заказа без его номера')
   def test_get_order_without_track(self):
      response = Methods.get_order_by_track("")
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для поиска" 

   @allure.title('Нельзя получить заказа с неверным номером')
   def test_get_orders_with_invalid_id(self):
      response = Methods.get_order_by_track(Person.track_invalid)
      assert response.status_code == 404
      assert response.json()["message"] == "Заказ не найден"

