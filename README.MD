установка зависимостей: заходим в директорию и вызываем pip install -r requirements

желательно установка пароля из окружения, и если приложение планируется к деплою то нужно добавить вторую строку с конфигурацией настроек
cd <папка для файла с паролями>
nano pswd
export SECRET_KEY = "django-insecure--a(imw-(fy(p+6_!^sqaby(3^euj(-ue!#_%&%or%m4##7b!nc"
export DJANGO_SETTINGS_MODULE = config.settings


разовая активация:
source pswd

постоянная активация
nano profile
source <папка для файла с паролями>/pswd


Если копирована текущая база данных то просто запускать:
запуск:  python manage.py runserver

Иначе для создания накатить миграции:
python manage.py makemigrations
ython manage.py migrate


Тестирование работы url (эндпоинтов)
тест запроса получение всех заданий:
curl http://127.0.0.1:8000/task/tasks/  

тест запроса получение одного задания:
curl -X GET  http://127.0.0.1:8000/task/tasks/1

тест заполнения post
curl http://127.0.0.1:8000/task/tasks/ -X POST -H "Content-Type: application/json" -d '{"title": "title_prdfdfdfojecmkt", "description": "description_prodffdject", "status": "false"}'

тест удаления:
curl -X DELETE  http://127.0.0.1:8000/task/tasks/2/

тест обновления:
curl http://127.0.0.1:8000/task/tasks/3/ -X PUT -H "Content-Type: application/json" -d '{"title": "title_prdfdfdfojecmkt", "description": "test"}'

Статусы ответов:
При успешном получениии списка или еденичного значения статус 200
при удалении 204
при создании/обновлении 201
при ошибках 400