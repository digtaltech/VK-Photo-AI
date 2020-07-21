# **VK-Photo-AI**

### Нейросеть по поиску лиц на фотографиях из Вконтакте


# Возможности

  - Выгрузка всех фотографий из диалога ВК
  - Скачивание ранее выгруженных фотографий
  - Поиск нужного человека на фотографиях с помощью библиотеки [face_recognition](https://github.com/ageitgey/face_recognition)


## Порядок действий
### Подготавливаем изображения
В скрипте **parse.py** в переменной **response** изменяем токен на свой

```python
    # Отправляем GET запрос на API и записываем ответ в response и запускаем скрипт
    response = requests.get(f"https://api.vk.com/method/messages.getHistoryAttachments?peer_id=2000000078&media_type=photo&start_from={next}&count=200&photo_size=1&preserve_order=1&max_forwards_level=44&v=5.103&access_token=ВАШ_ТОКЕН")
    items = json.loads(response.text) # Считываем ответ от сервера в формате JSON
```

После выполнения у нас заполнится файл **input.txt** ссылками для скачивания изображений.

Запускаем скрипт **download.py**. Он загрузит все фотографии по ссылкам из **input.txt**  в папку **img**

### Работаем с нейросетью

Для поиска человека по изображениям необходимо взять изображение необходимого  человека (желательно хорошего качества в анфас)
И поместить это изображение в папку **face**

В файле **search.py** в переменной find_face указываем путь до изображения человека, которого мы ищем.
```python
find_face = face_recognition.load_image_file("face/your_photo.jpg") # Загружаем изображение нужного человека
face_encoding = face_recognition.face_encodings(find_face)[0] # Кодируем уникальные черты лица, для того чтобы сравнивать с другими
```

Запускаем скрипт и ожидаем окончания процесса
### Глубокий анализ

Если хотите увеличить качество поиска человека, можно подключить к поиску видеокарту **Nvidia** с технологией CUDA
Для этого надо добавить параметр model= «cnn» и изменить фрагмент кода в файле **search.py** для изображения с которым хотим искать нужного человека:
```python
    unknown_picture = face_recognition.load_image_file(f"img/{i}.jpg") # Загружаем скачанное изображение
    face_locations = face_recognition.face_locations(unknown_picture, model= "cnn") # Подключаем ускорение GPU
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture) # Кодируем уникальные черты лица
```
