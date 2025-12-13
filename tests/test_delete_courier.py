import requests
from methods.methods import Methods
import allure

class TestDeleteCourier:

   @allure.title('Успешное удаление курьера')
   def test_delete_courier(self, create_courier_and_return_id):
      response = Methods.delete_courier(create_courier_and_return_id)
      assert response.status_code == 200
      assert response.json() == {"ok": True }

   @allure.title('Нельзя удалить курьера без id курьера')
   def test_delete_courier_without_id(self):
      response = Methods.delete_courier('')
      assert response.status_code == 400, f"Code:{response.status_code}"
      assert response.json()["message"] == "Недостаточно данных для удаления курьера", f"{response.json()}"

   @allure.title('Нельзя удалить курьера с несуществующим id курьера')
   def test_delete_courier_with_invailid_id(self):
      response = Methods.delete_courier('19999999')
      assert response.status_code == 404
      assert response.json()["message"] == "Курьера с таким id нет."

