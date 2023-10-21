import configuration
import data
import requests
import pytest
# Выполняем запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL+configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.order_body)
# Сохраняем трек-номер заказа как переменную
track = response.json()['track']

# Выполняем запрос на получение заказа по трек-номеру
def get_order_by_track():
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH + str(track)
                )

# Тест 1. Получение кода 200 на запрос на получение заказа по трек-номеру
def test_status_200():
    assert get_order_by_track().status_code == 200


