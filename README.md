# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве.

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/0rcb0n3-lab/ya_afisha.git
cd ya_afisha
```

### 2. Создать и активировать виртуальное окружение

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

На Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Скопируйте шаблон в корень проекта:

```bash
cp .env.example .env
```

Или создайте файл `.env` в корне проекта (рядом с `manage.py`):

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
PLACES_DIRECTORY_URL=https://api.github.com/repos/devmanorg/where-to-go-places/contents/places
```

### 5. Применение миграций

```bash
python manage.py migrate
```

### 6. Создание администратора

```bash
python manage.py createsuperuser
```

### 7. Запуск сервера

```bash
python manage.py runserver
```

Сайт будет доступен по адресу:

http://127.0.0.1:8000/

Административная панель:

http://127.0.0.1:8000/admin/

## Загрузка мест

Для загрузки места из JSON-файла по ссылке используйте команду:

```bash
python manage.py load_place "URL_JSON"
```

Например:

```bash
python manage.py load_place "https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json"
```

Можно передать несколько ссылок сразу:

```bash
python manage.py load_place "URL_1" "URL_2"
```

Для загрузки всех мест из репозитория:

```bash
python manage.py load_places_bulk
```

Адрес репозитория с JSON-файлами задаётся переменной `PLACES_DIRECTORY_URL` в файле `.env`:

```env
PLACES_DIRECTORY_URL=https://api.github.com/repos/devmanorg/where-to-go-places/contents/places
```

Если источник данных изменится, достаточно заменить значение `PLACES_DIRECTORY_URL` в `.env` и повторить запуск.

При повторном запуске уже загруженные места не создаются повторно.

## Формат JSON

Пример файла с локацией:

```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий.",
    "description_long": "Рядом со станцией метро «Войковская» открылось антикафе Bizone...",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).