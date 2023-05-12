# API FINAL YATUBE 

Применил: Python 3.9.13, DRF, SQLite

# Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:ValeryKorobov/api_final_yatube.git
```

- Cоздать и активировать виртуальное окружение (На Windows):
```
python -m venv venv
source venv/Scripts/activate
```
- Cоздать и активировать виртуальное окружение (На Linux):
```
python3 -m venv venv
source env/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```

# Пример GET-запроса к API:

- Получить список всех постов, эндпоинт /api/v1/posts/:
```
[
    {
        "id": 2,
        "author": "New_user",
        "image": "http://127.0.0.1:8000/media/posts/images/temp_OIh4P08.png",
        "comments": [
            "Comment object (2)",
            "Comment object (3)"
        ],
        "text": "Второй пост с тем же котиком без группы",
        "pub_date": "2023-05-12T16:51:14.907711Z",
        "group": null
    }
]
```