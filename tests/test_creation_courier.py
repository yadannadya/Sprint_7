
import pytest
from methods.methods import Methods
import helpers
import allure

from data import Person


class TestCreationCourier:

   @allure.title('Успешная регистрация курьера')
   def test_create_courier_success(self):
      response = Methods.create_courier(body=helpers.faker_courier())
      assert response.status_code == 201
      assert response.json() == {"ok": True}
   
   @allure.title('Нельзя зарегистрировать 2 курьеров с одинаковым логином')
   def test_create_courier_with_repeat_login_unsuccess(self):
      body = helpers.faker_courier()
      Methods.create_courier(body=body)
      response_2 = Methods.create_courier(body=body)
      assert response_2.status_code == 409
      assert response_2.json()["message"] == "Этот логин уже используется"

   @allure.title('Нельзя зарегистрировать курьера без логина или пароля')
   @pytest.mark.parametrize('body', Person.invalid_courier)
   def test_create_courier_invalid_body_unsuccess(self, body):
      response = Methods.create_courier(body=body)
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для создания учетной записи" 

