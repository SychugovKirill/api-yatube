# api_final

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone https://github.com/SychugovKirill/api-yatube.git
```

```sh
cd api-yatube
```

Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv .venv
```

```sh
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python3 manage.py migrate
```

Запустить проект:

```sh
python3 manage.py runserver
```
