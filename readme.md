
# welcome fool! 
congratulations! you find the source code




```
virtualenv -p python3 venv
    pip freeze > requirements.txt


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