# Описание

Проект представляет собой API для проекта Yatube.

##### Реализован функционал дающий возможность:
* Подписываться на пользователя.
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.

У неаутентифицированных пользователей доступ к API только на чтение. Исключение — эндпоинт /follow/.

Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

## Стек технологий

* Python 3.11,
* Django 4.2,
* DRF,
* JWT + Djoser

## К API есть документация по адресу `http://localhost:8000/redoc/`

# Установка

- Склонировать репозиторий: python -m venv venv
- Создать и активировать виртуальное окружение для проекта (версия не ниже Python 3.7):
source venv/scripts/activate

## 3) Установить зависимости
python pip install -r requirements.txt

## 4) Сделать миграции
python manage.py makemigrations
python manage.py migrate

## 5) Запустить сервер
python manage.py runserver

# Примеры

Для доступа к API необходимо получить токен: 
Нужно выполнить POST-запрос localhost:8000/api/v1/token/ передав поля username и password. API вернет JWT-токен

Дальше, передав токен можно будет обращаться к методам, например: 

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>

# Автор 
Хитяев Кирилл 