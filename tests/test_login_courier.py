import requests
from methods.methods import Methods
import pytest
import allure
import helpers
from data import Person


class TestLoginCourier:

   @allure.title('Успешная авторизация зарегистрированного курьера')
   def test_login_courier_success(self):
      body = helpers.faker_courier()
      Methods.create_courier(body=body)
      response = Methods.login_courier(body={"login": body["login"],
                                             "password": body["password"]})
      assert response.status_code == 200
      assert "id" in response.json()

   @allure.title('Ошибка авторизации при отсутствии логина')
   def test_login_courier_without_login_unsuccess(self):
      body = helpers.faker_courier()
      response = Methods.login_courier(body={"password": body["password"]})
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для входа" 

   @allure.title('Ошибка авторизации при отсутствии пароля')
   def test_login_courier_without_password_unsuccess(self):
      body = helpers.faker_courier()
      response = Methods.login_courier(body={"login": body["login"],
                                             "password": ""})
      assert response.status_code == 400
      assert response.json()["message"] == "Недостаточно данных для входа" 


   @allure.title('Ошибка авторизации для незарегистрированного курьера')
   def test_login_not_registered_courier_unsuccess(self):
      body = helpers.faker_courier()
      response = Methods.login_courier(body={"login": body["login"],
                                             "password": body["password"]})
      assert response.status_code == 404
      assert response.json()["message"] == "Учетная запись не найдена"