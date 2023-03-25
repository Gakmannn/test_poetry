#Шаг 1

Установить poerty
```
pip install poetry
```
Если poetry не найден после установки, запустить
```
pip install poetry --user
```
И добавить папуку в PATH, перезапусть vs code

Проверить версию python в poetry.lock и pyproject.toml

#Шаг 2
Запустить команду

```
poetry shell
poetry install
```

Перейти в папку metanit
```
cd metanit
```
Запустить сервер
```
python manage.py runserver
```

Создать миграции

```
python manage.py makemigrations
python manage.py migrate
```