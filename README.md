# Stepee
Educational web service

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