# Проект books_list:

### Бэкенд и фронтенд для управления списком книг.

[Тестовое задание](https://docs.google.com/document/d/14RZ3VrzoIw4NWBAUkiuBbTnU2j1Seg_z9OReJceEP9c/edit)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v4.2.6-blue?logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-v3.14.0-blue?logo=DRF)](https://www.django-rest-framework.org/)

**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)



**CI/CD:**

[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?logo=Yandex)](https://cloud.yandex.ru/)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?logo=Telegram)](https://core.telegram.org/api)

[⬆️Оглавление](#оглавление)
</details>

<br>

## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь:
 - создал аккаунт [DockerHub](https://hub.docker.com/), если запуск будет производиться на удаленном сервере.
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```bash
    docker --version && docker-compose --version
    ```
<h1></h1>
</details>

<details><summary>Локальный запуск</summary> 

**!!! Для пользователей Windows обязательно выполнить команду:** 
```bash
git config --global core.autocrlf false
```
иначе файл start.sh при клонировании будет бракован.

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```bash
git clone https://github.com/daniilbp/Django-books_list.git && \
cd Django-books_list && \
cp env_example .env && \
nano .env
```
<details><summary>Локальный запуск: Django/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```bash
python books_list/manage.py makemigrations && \
python books_list/manage.py migrate && \
python books_list/manage.py load_data && \
python books_list/manage.py create_superuser && \
python books_list/manage.py runserver
```
Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
 </details>

<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу `http://localhost`.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```
</details><h1></h1></details>

<details><summary>Запуск на удаленном сервере</summary>

1. Сделайте [форк](https://docs.github.com/en/get-started/quickstart/fork-a-repo) в свой репозиторий.

2. Создайте `Actions.Secrets` согласно списку ниже (значения указаны для примера) + переменные окружения из env_example файла:
```py
PROJECT_NAME
SECRET_KEY

POSTGRES_PASSWORD
DATABASE_URL

CODECOV_TOKEN

DOCKERHUB_USERNAME
DOCKERHUB_PASSWORD

# Данные удаленного сервера и ssh-подключения:
HOST  # публичный IP-адрес вашего удаленного сервера
USERNAME
SSH_KEY  
PASSPHRASE

# Учетные данные Телеграм-бота для получения сообщения о успешном завершении workflow:
TELEGRAM_USER_ID
TELEGRAM_BOT_TOKEN
```

3. Запустите вручную `workflow`, чтобы автоматически развернуть проект в трех docker-контейнерах (db, web, nginx) на удаленном сервере.
</details><h1></h1>

При первом запуске будут автоматически произведены следующие действия:
  - выполнены миграции БД
  - БД заполнена начальными данными
  - собрана статика
  - создан суперюзер (пользователь с правами админа) с учетными данными:
      - для Django: username = 'adm', password = 'adm' - значения можно изменить в `books_list\bookapp\management\commands\create_superuser.py`
      - для Docker Compose - из переменных окружения `ADMIN_USERNAME`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`
      
 

Список книг и управление ими, а также список профилей и управление ими ч/з ресурс book представлены по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/books/main/
  - http://localhost/books/main/
  - `http://<IP-адрес удаленного сервера>/books/main/`

Отдельный список профилей и управление ими ч/з отдельный ресурс profile представлены по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/books/main/update_profiles/
  - http://localhost/books/main/update_profiles/
  - `http://<IP-адрес удаленного сервера>/books/main/update_profiles/`

Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/admin/
  - http://localhost/admin/
  - `http://<IP-адрес удаленного сервера>/admin/`

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

На странице `http://<hostname>/books/main/` представлен список из десяти тестовых книг, и кнопки для управления ими: изменить, удалить и добавить новую, а также список из шести профилей (колонок книг) с возможностью редактирования их параметра видимости.
###### При клике на `Изменить` происходит переход на страницу с заполненной формой книги готовой к редактированию. Возврат к списку книг происходит при клике `Вернуться к списку книг`.
###### При клике на `Удалить` происходит удаление книги и обновление страницы списка книг.
###### При клике на `Добавить книгу` происходит переход на страницу с пустой формой книги готовой к заполнению. Возврат к списку книг происходит при клике `Вернуться к списку книг`.
###### При клике на `Применить` в форме скрытия столюцов происходит обновление значения параметров видимости профилей и обновление страницы списка книг с учетом видимости колонок.
###### При клике на `Управление видимостью` происходит переход на страницу `http://127.0.0.1:8000/books/main/update_profiles/`, на которой в форме скрытия столюцов при клике на `Применить` происходит обновление значения параметров видимости профилей. Возврат к списку книг происходит при клике `Вернуться к списку книг`.


[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Для удаления проекта выполните следующие действия:
```bash
cd .. && rm -fr Django-books_list && deactivate
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Danii Boyko](https://github.com/daniilbp)

[⬆️В начало](#Проект)
