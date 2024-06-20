import requests # подтягиваю библиотеку
from configuration import create, get_information # импортирую ручки из configuration
def create_order(order_body):        # создается заказа
    response_create = requests.post(create, json=order_body)
    return response_create
  

def get_order(track):    # получение информации о заказе по номеру
    url = get_information + str(track)
    response_get = requests.get(url)
    return response_get




