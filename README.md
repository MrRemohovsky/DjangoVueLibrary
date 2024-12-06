DjangoVueLibrary — это веб-приложение (пет-проект) для управления библиотечным каталогом с поддержкой авторизации и кэширования.

Проект создан с использованием следующих технологий:
-Серверная часть: Django, Django REST Framework
-Интерфейс: Vue.js
-База данных: SQLite
Дополнительно:
-Celery – для обработки фоновых задач (используется для задачи по отправке email пользователю)
-Redis – для кэширования и брокера задач
-Docker – для контейнеризации

Для работы с проектом на вашем устройстве должны быть установлены:
-Docker и Docker Compose
-Git

Для клонирования репозитория:
git clone https://github.com/MrRemohovsky/DjangoVueLibrary.git

Запуск контейнеров:
-Далее cd DjangoVueLibrary
-docker-compose build
-docker compose up

Бэк на порту 8000, фронт на 8080
---------------------------------
СУПЕРПОЛЬЗОВАТЕЛЬ: locallibrary 
password: locallibrary
------------------------
ПОЛЬЗОВАТЕЛЬ: testuser1
password: locallibrary1
email: locallibrarytestuser1@mail.ru

Сброс пароля по почте: email приходит в консоль
