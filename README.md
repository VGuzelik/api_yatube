# Проект yatube

Представляет собой социальную сеть для публикации личных дневников.

Api_yatube позволяет зарегистрироваться новому пользователям, просматривать все посты авторов, посты определенного автора, создавать обновлять, удалять, комментировать посты и подписываться на авторов.

*Когда вы запустите проект, по адресу  [http://127.0.0.1:8000/redoc/] будет доступна документация*


> **Как запустить проект**:
>>Клонировать репозиторий и перейти в него в командной строке:

    git clone https://github.com/Guzelik-Victor/api_final_yatube.git

    cd kittygram



>Cоздать и активировать виртуальное окружение:

  `python3 -m venv env`

  `source env/bin/activate`

>Установить зависимости из файла requirements.txt:

  `python3 -m pip install --upgrade pip`

  `pip install -r requirements.txt`

>Выполнить миграции:

  `python3 manage.py migrate`

> Запустить проект:

  `python3 manage.py runserver`
  
