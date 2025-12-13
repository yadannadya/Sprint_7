import requests
from curl import Url
import allure

class Methods:
      
   @staticmethod 
   @allure.step('Создать курьера')
   def create_courier(body):
      return requests.post(Url.courier, json=body)
    

   @staticmethod
   @allure.step('Создать заказ')
   def create_order(body):
      return requests.post(Url.order, json=body)
   
   @staticmethod
   @allure.step('Авторизовать курьера')
   def login_courier(login, password):
      body = {
            "login": login,
            "password": password
        }
      return requests.post(Url.login_courier, json=body)
   
   @staticmethod
   @allure.step('Получить список заказов')
   def get_list_order():
      return requests.get(Url.order)
   
   @staticmethod 
   @allure.step('Удалить курьера')
   def delete_courier(id_courier):
      return requests.delete(f"{Url.courier}/{id_courier}")
    
   @staticmethod 
   @allure.step('Получить заказ по его номеру')
   def get_order_by_track(track):
      return requests.get(f"{Url.track}{track}")
   

   @staticmethod 
   @allure.step('Удалить заказ')
   def delete_order(track):
      return requests.put(f"{Url.delete_order}?track={track}")
   

   @staticmethod 
   @allure.step('Принять заказ')
   def accept_orders(id_order, id_courier):
      return requests.put(f"{Url.accept_order}{id_order}?courierId={id_courier}")
      