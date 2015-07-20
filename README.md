# Sportcourts
Social sport service

# Установка и настройка #
1) Установка Gulp в директории проекта
`npm install --save-dev gulp`

2) Create virtualenv (Project Interpreteur)
```
install django
install django-phonenumber-field
```

3) Далее в директории проекта делаем
`npm init`

4) Далее следует установить плагины Gulp(это может быть долго):
```
npm i gulp-autoprefixer --save
npm i gulp-minify-css --save
npm i gulp-imagemin --save
npm i imagemin-pngquant --save
npm i gulp-uglify --save
npm i rimraf --save
npm i gulp-sass --save
npm i gulp-sourcemaps --save
npm i gulp-rigger --save
npm i gulp-watch --save
npm i gulp-jade --save
```

5) Далее нужен пакетный менеджер bower для удобной работы с версиями библиотек:
`bower init`

6) Далее устанавливаем все зависимости:
```
bower install bootstrap-sass --save
bower install jquery-ui --save
bower install fontawesome --save
bower install social-likes --save
```

7) Для обновления зависимоcтей юзаем
```
npm update --save
npm outdated
```

8) Install postgres (`brew install postgres`)
`initdb /usr/local/var/vitaliyharchenko
createdb
psql
CREATE USER sc WITH PASSWORD '4203';
CREATE DATABASE sc OWNER sc;
ALTER USER sc CREATEDB;`

9) install psycopg2
```
cd venv
source bin/activate
cd
cd Dev/sportcourts
pip install psycopg2
```

10) Миграция
```
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
```

# Работа с Git #
```
git status
git add
git commit -m ''
git push
```

# Работа с БД #
```
psql
DROP DATABASE sc;
CREATE DATABASE sc OWNER sc;
ALTER USER sc CREATEDB;
python manage.py makemigrations customuser
python manage.py migrate customuser
python manage.py syncdb
python manage.py makemigrations courts
python manage.py migrate courts --fake-initial
python manage.py syncdb
```

# Работа с удаленкой #
```
lt --port 8000
```

# Работа с зависимостями #
```
Длясоздания файла зависимостей
pip freeze > requirements.txt
```


# Работа с сервером test.sportcourts.ru #
```
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
```
1) Установка Ubuntu ubuntu14.04-x86_64
2) ssh root@194.58.108.127
3) sudo apt-get update
4) sudo apt-get upgrade
5) restart server
6) sudo apt-get install python-virtualenv
7) sudo virtualenv /opt/scenv
8) source /opt/scenv/bin/activate
9) pip install django
10) deactivate
11) sudo apt-get install libpq-dev python-dev
12) sudo apt-get install postgresql postgresql-contrib
13) sudo apt-get install nginx
14) source /opt/scenv/bin/activate
15) pip install gunicorn
16) deactivate
17) sudo su - postgres
18) createdb scdb
19) createuser --interactive scuser (n n n)
20) psql
21) GRANT ALL PRIVILEGES ON DATABASE scdb TO scuser;
22) \q
23) su - root
24) sudo nano /etc/nginx/sites-available/sportcourts
25) 
```
server {
    server_name test.sportcourts.ru;

    access_log off;

    location /static/ {
        alias /opt/sportcourts/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}
```
26) cd /etc/nginx/sites-enabled
27) sudo ln -s ../sites-available/sportcourts
28) sudo service nginx restart
29) sudo apt-get install git
30) cd /opt/
31) git clone https://github.com/vitaliyharchenko/sportcourts.git
32) source /opt/scenv/bin/activate
33) pip install -r /opt/sportcourts/requirements.txt
34) cd /opt/sportcourts
35) gunicorn sportcourts.wsgi:application --bind=127.0.0.1:8001 --daemon

36) apt-get install npm


