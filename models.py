from app import db
from datetime import datetime
import re


def slugify(text):
    pattern = r'[^\w+\-]'
    return re.sub(pattern, '-', text.lower())


class Category(db.Model):
    # __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer(), unique=True)
    title = db.Column(db.String(256), unique=True)
    title_ru = db.Column(db.String(256), unique=True)
    slug = db.Column(db.String(256), unique=True)
    main_page_card_text = db.Column(db.Text)
    text = db.Column(db.Text)
    # problems = db.relationship('Problem', backref='Categories', lazy=True)
    problems = db.relationship('Problem', backref='Categories', lazy='dynamic')

    created = db.Column(db.DateTime, default=datetime.now)

    # def __init__(self, number, title, slug):
        # self.number = number
        # self.title = title
        # self.slug = slug

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()

    def __repr__(self):
        return '<Category id={}, title="{}">'.format(self.id, self.title)

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


class Problem(db.Model):
    # todo: make category many to many
    # todo: add i met this question filed (button)
    # todo: make hashtags for categories

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer(), unique=True)
    level = db.Column(db.Integer(),)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String(256), unique=True)
    text = db.Column(db.Text)
    answer = db.Column(db.Text)
    knowledge = db.Column(db.Text)
    advises = db.Column(db.Text)
    theme = db.Column(db.Text)
    code = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(Problem, self).__init__(*args, **kwargs)
        self.generate_number()

    def __repr__(self):
        return '<Problem id={}, title="{}">'.format(self.id, self.title)

    def generate_number(self):
        self.number = self.id


# todo: separate questions by positions. Exsamples: web-developer, back-end developer, data science...
# todo: add companies that answer this question (this might be anonymous?)
