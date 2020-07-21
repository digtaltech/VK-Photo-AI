import urllib.request

f = open('input.txt') # Наш файл с ссылками

val = 1 # Переменная для счётчика
for line in f: # Перебираем файл построчно
    line = line.rstrip('\n')
    # Скачиваем изображение в папку "img"
    urllib.request.urlretrieve(line, f"img/{val}.jpg")
    print(val,':','скачан') # В логи выводим сообщение о загрузке
    val += 1 # Увеличиваем счётчик
print("Готово")
