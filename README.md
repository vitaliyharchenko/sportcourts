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

# Работа с сервером test.sportcourts.ru #
```
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
```
1) Установка Ubuntu 12.04
2) ssh root@194.58.108.127
3) sudo apt-get update
4) sudo apt-get upgrade
5) sudo apt-get install python-virtualenv
6) sudo virtualenv /opt/myenv
7) source /opt/myenv/bin/activate
8) pip install django
9) deactivate
10) sudo apt-get install libpq-dev python-dev
11) sudo apt-get install postgresql postgresql-contrib
12) sudo apt-get install nginx
13) source /opt/myenv/bin/activate
14) pip install gunicorn
15)
```
sudo su - postgres
createdb scdb
createuser -P
scuser, 4203, nnn
psql
GRANT ALL PRIVILEGES ON DATABASE scdb TO scuser;
sudo nano /etc/nginx/sites-available/sportcourts
```

```
/opt/scenv
```