import requests

class Url:

    url = 'https://qa-scooter.praktikum-services.ru/'
    courier = f'{url}api/v1/courier'
    login_courier = f'{url}api/v1/courier/login'
    order = f'{url}api/v1/orders'
    track = f'{url}api/v1/orders/track?t='
    delete_order = f'{url}api/v1/orders/cancel'
    accept_order = f'{url}api/v1/orders/accept/'