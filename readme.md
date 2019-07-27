
# welcome fool! 
congratulations! you find the source code of Kaban project


Проект работатет на 3 питоне 


# Fast commands

    pip freeze > requirements.txt

    python manage.py db init
    
    python manage.py db migrate
    
    python manage.py db upgrade

# Start 

https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18


Use `brew install` for OsX)
Use `apt-get` for Linux)



Установить системные пакеты (server only)

    sudo apt-get install software-properties-common
    sudo apt-add-repository universe
    sudo apt-get update
    sudo apt-get install nginx supervisor python3-dev libpq-dev python-pip python-virtualenv postgresql postgresql-contrib git -y
        
    pip install psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Script


Установить и настроить PostgreSQL

    sudo apt-get install postgresql -y
    sudo su - postgres
    psql
    CREATE DATABASE kaba_db;
    CREATE USER kaba_db_user WITH PASSWORD 'InterViewsMakeMe8annaDie';
    GRANT ALL PRIVILEGES ON DATABASE kaba_db TO kaba_db_user;
    \q
    exit



Клонировать проект (удостоверься, что в кабинете есть ssh ключ для сервака)

    git clone git@gitlab.com:Kusko/kaba.git

Создать и активировать виртуальное окружение 
    
    virtualenv --no-site-packages -p python3 venv
    source venv/bin/activate


установить зависимости и мигрировать миграции


    pip install -r requirements.txt
    
    (
        flask_alchemydumps багается, ннужно поменять импорт
        ToDo: обновить до новой версии библиотеку, где не этого бага нет
    )
        nano /root/kaba/venv/lib/python3.6/site-packages/flask_alchemydumps/__init__.py
        поменяй
        >>>  from flask.ext.script import Manager  ->  from flasl_script import Manager

(Если 1 раз)

    export APP_SETTINGS="config.DevelopmentConfig"
    python manage.py db init
python manage.py db init

python manage.py db migrate

python manage.py db upgrade


# temporary code (do not touch pls)
```


virtualenv -p python3 venv

pip freeze > requirements.txt
pip install -r requirements.txt


export FLASK_APP=kaba.py
flask run


https://flask.palletsprojects.com/en/1.0.x/quickstart/#debug-mode
export FLASK_ENV=development
or 
python app.py

pip install psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Script


brew reinstall postgresql
psql
CREATE DATABASE kaba_db;
CREATE USER kaba_db_user WITH PASSWORD 'InterViewsMakeMe8annaDie';
GRANT ALL PRIVILEGES ON DATABASE kaba_db TO kaba_db_user;
\q
exit

export DATABASE_URL="postgres://kaba_db_user:InterViewsMakeMe8annaDie@localhost:5432/kaba_db"
export APP_SETTINGS="config.DevelopmentConfig"

python manage.py db init

python manage.py db migrate

python manage.py db upgrade


python manage.py runserver




save first category
    from app import models, db
    category = models.Category(title='Python', text='qwe', main_page_card_text='asd')
    category
    >>> <Category id None>
    db.session.add(category)
    db.session.commit()
    category
    >>> <Category id 1>

```



Создание Категорий на основе вопросов
```
def asd():
    from app import app, db
    from models import Category, Problem

    problems_ = Problem.query.all()
    anknown_category = Category(title='Unknown category')
    db.session.add(anknown_category)
    db.session.commit()

    for problem_ in problems_:

        if problem_.theme:
            category_title = problem_.theme
            if category_title == 'Логическая задачка':
                category_title = 'Логическиие задачки'
            if category_title == 'Знание python':
                category_title = 'Структуры данных'
            if category_title == 'Задачка на алгоритмы' or category_title == 'Задачка на алгоритмы/Python':
                category_title = 'Алгоритмы'

            category_slug = slugify(category_title)
            if category_slug == 'python-':
                category_slug = 'python'
                category_title = 'Python'

            category = Category.query.filter_by(slug=category_slug).first()
            if not category:
                category = Category(title=category_title)
                db.session.add(category)
                db.session.commit()
            p = Problem.query.filter_by(id=problem_.id).first()
            p.category_id = category.id
            p.theme = ''
            db.session.commit()
        else:
            problem_.category_id = anknown_category.id
            db.session.commit()

```

https://pypi.org/project/Flask-AlchemyDumps/0.0.3/



import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=kaba_db")
    conn.close();
except psycopg2.OperationalError as ex:
    print("Connection failed: {0}".format(ex))
    