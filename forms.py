
from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField


class ProblemForm(Form):
    title = StringField('Title')
    text = TextAreaField('Text')
    category = IntegerField('Category')
    answer = TextAreaField('Answer')
    knowledge = TextAreaField('Knowledge')
    advises = TextAreaField('Advises')
