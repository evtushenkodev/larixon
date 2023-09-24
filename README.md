# Тестовое задание Larixon

В данном проекте используется DjangoREST Framework, PostgreSQL, Nginx, Docker.

### Для запуска проекта вам потребуется выполнить следующие комманды:

## Клонирование репозитория

Для начала работы с проектом, склонируйте его себе на локальный компьютер:

```bash
git clone https://gitlab.com/maxcrimea/larixon-test.git
cd larixon_test
```

## Настройка окружения

Создайте файл .env в корневой директории проекта, используя env.example как шаблон.

## Запуск проекта

Для запуска проекта используйте Docker Compose:

```bash
docker-compose up -d
```

После успешного запуска, проект будет доступен по адресу 

Admin панель: http://localhost:8888/admin

Список объявлений: http://localhost:8888/api/v1/advert-list/

Объявление с id=1: http://localhost:8888/api/v1/advert/1/

## Запуск тестов

Для запуска тестов выполните следующую команду:

```bash
docker-compose exec django python manage.py test
```