import json
import requests

next = None # Переменная в которую будем записывать ключ смещения
def newfunc():
    val = 1 # Переменная для счётчика
    global next
    Fin = open("input.txt","a") # Создаём файл для записи ссылок
    # Отправляем GET запрос на API и записываем ответ в response
    response = requests.get(f"https://api.vk.com/method/messages.getHistoryAttachments?peer_id=2000000078&media_type=photo&start_from={next}&count=200&photo_size=1&preserve_order=1&max_forwards_level=44&v=5.103&access_token=ВАШ_ТОКЕН")
    items = json.loads(response.text) # Считываем ответ от сервера в формате JSON

    if items['response']['items'] != []: # Проверка наличия данных в массиве
        for item in items['response']['items']: # Перебираем массив items
            link = item['attachment']['photo']['sizes'][-1]['url'] # Записываем самый последний элемент, так как он самого максимального расширения
            print(val,':',link) # Лог перебора фотографий
            val += 1 # Увеличиваем значение счётчика
            Fin.write(str(link)+"\n") # Записываем новую строку в файл
        next = items['response']['next_from'] # Записываем ключ для получения следующих фотографий
        print('dd',items['response']['next_from'])
        newfunc() # Вызываем функцию
    else: # В случае отсутствия данных
        print("Получили все фото")

newfunc()
