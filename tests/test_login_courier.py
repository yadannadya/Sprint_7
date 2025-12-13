import requests
from methods.methods import Methods
import pytest
import allure
import helpers
from data import Person


class TestLoginCourier:

   @allure.title('Успешная авторизация зарегистрированного курьера')
   def test_login_courier_success(self, generate_courier_and_delete):
      Methods.create_courier(body=generate_courier_and_delete[0])
      response = Methods.login_courier(generate_courier_and_delete[1], generate_courier_and_delete[2])
      assert response.status_code == 200
      assert "id" in response.json()

   @allure.title('Ошибка авторизации при отсутствии логина или пароля')
   @pytest.mark.parametrize('login, password', Person.invalid_login)
   def test_login_courier_invalid_body_unsuccess(self, login, password):
      response = Methods.login_courier(login, password)
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для входа"  

   
   @allure.title('Ошибка авторизации для незарегистрированного курьера')
   def test_login_not_registered_courier_unsuccess(self):
      body = helpers.faker_courier()
      response = Methods.login_courier(login = body["login"], password = body["password"])
      assert response.status_code == 404
      assert response.json()["message"] == "Учетная запись не найдена"