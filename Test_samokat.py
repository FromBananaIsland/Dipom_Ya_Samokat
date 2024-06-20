# Дмитрий Лагунов, 17-я когорта — Финальный проект. Инженер по тестированию плюс
# У меня нет стрелочки питеста перед функцией с тестом на скрине, но запускается именно питест, судя по логам теста.
from data import order_body # импортирую тело заказ
from sender_stand_request import create_order, get_order # импортирую функции создание заказ и получение инфы по номеру


def test_zakaz_sozdanie_i_poluchenie_infi_po_nomeru():
    response_create = create_order(order_body)   # Запрос на создание заказа
    order_track = response_create.json()["track"] # Сохраняется номер трека заказа
    response_get = get_order(order_track)         # Выполняется запрос на получения заказа по треку
    assert response_get.status_code == 200     # Проверяется, что код ответа равен 200.
    
