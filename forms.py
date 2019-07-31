
from wtforms import Form, IntegerField, SelectField, StringField, TextAreaField


class ProblemForm(Form):
    # todo: make level choice field
    # todo: make category choice field

    title = StringField('Title')
    level = StringField('Level 1-3 please')
    text = TextAreaField('Text')
    category = IntegerField('Category')
    answer = TextAreaField('Answer')
    knowledge = TextAreaField('Knowledge')
    advises = TextAreaField('Advises')
