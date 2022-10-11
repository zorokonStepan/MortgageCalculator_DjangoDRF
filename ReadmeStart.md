<ol>
    <li><b>python -m venv venv</b> - создать виртуальное окружение</li><br>
    <li><b>.\venv\Scripts\activate</b> - активировать виртуальное окружение</li><br>
    <li><b>python.exe -m pip install --upgrade pip</b> - обновить менеджер пакетов</li><br>
    <li><b>pip install django</b> - установить библиотеку Django</li><br>
    <li><b>pip install djangorestframework</b> - установить библиотеку DRF</li><br>
    <li><b>pip install environs</b> - установить библиотеку environs</li><br>
    <li><b>django-admin startproject mortgage</b></li><br>
    <li><b>cd mortgage</b></li><br>
    <li><b>Установить PostgreSQL. Создать БД.</b></li><br>
    <li><b>pip install psycopg2</b> - установить библиотеку psycopg2 для работы с PostgreSQL</li><br>
    <li><b>Создать файл .env и прописать в него данные. в env_example указано какие<br>
        SECRET_KEY= - ключ Django<br>
        <br>
        Параметры БД:<br>
        NAME=<br>
        USER=<br>
        PASSWORD=<br>
        HOST=<br>
        PORT=<br></b></li><br>    
    <li><b>python manage.py migrate</b> - чтоб заработали базовые приложения Django сделать миграции базовых таблиц в БД</li><br>
    <li><b>python manage.py runserver</b> - проверим все ли прошло успешно</li><br>
    <li><b>INSTALLED_APPS = […] строку 'rest_framework'</b> - регистрируем DRF</li><br>
    <li>Скопировать код с репозитория</li>
    <li><b>python manage.py makemigrations</b> - создать миграции для созданных таблиц</li><br>
    <li><b>python manage.py migrate</b> - выполнить миграции</li><br>
    <li><b>python manage.py createsuperuser</b> - теперь можно зайти в админку</li><br>
</ol>