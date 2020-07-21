import json
import requests

val = 1 # Переменная для счётчика

Fin = open("input.txt","a") # Создаём файл для записи ссылок
# Отправляем GET запрос на API и записываем ответ в response
response = requests.get("https://api.vk.com/method/messages.getHistoryAttachments?peer_id=2000000078&media_type=photo&start_from=&count=10&photo_size=1&preserve_order=1&max_forwards_level=45&v=5.103&access_token=ВАШ_ТОКЕН")
items = json.loads(response.text) # Считываем ответ от сервера в формате JSON

# Так как по GET запросу сервер возвращает в каждом элементе массив с картинкой в разных размерах, будем перебирать всё циклом

for item in items['response']['items']: # Перебираем массив items
    link = item['attachment']['photo']['sizes'][-1]['url'] # Записываем самый последний элемент, так как он самого максимального расширения
    print(val,':',link) # В консоли выводим лог по проделанной работе
    Fin.write(str(link)+"\n") # Записываем новую строку в файл
    val += 1 # Увеличиваем значение счётчика
