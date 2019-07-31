# -*- coding: utf-8 -*-
from flask import redirect, render_template, request, url_for
from sqlalchemy.sql.expression import func, select

from app import app, db
from forms import ProblemForm
from models import Category, Problem


def get_common_data():
    problems_ = Problem.query

    data = {
        'categories': Category.query.all(),
        'all_problems_qty': len(problems_.all()),
        'junior_problems_qty': len(problems_.filter_by(level=1).all()),
        'middle_problems_qty': len(problems_.filter_by(level=2).all()),
        'senior_problems_qty': len(problems_.filter_by(level=3).all()),
        'legend_problems_qty': len(problems_.filter_by(level=4).all()),
        'insane_problems_qty': len(problems_.filter(Problem.level >= 4).all())
    }

    return data


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/')
def main_page():
    context = get_common_data()
    return render_template('main_page.html', context=context)\


@app.route('/about_us')
@app.route('/about_us/')
def about_us():
    context = get_common_data()
    return render_template('about_us.html', context=context)


@app.route('/problems/')
@app.route('/problems/<slug>')
@app.route('/problems/<slug>/')
def problems(slug=None):
    context = dict()

    if slug:
        category = Category.query.filter_by(slug=slug).first()
        problems_ = Problem.query.filter_by(category_id=category.id).order_by(Problem.created).all()

        context['category'] = category
    else:
        problems_ = Problem.query.all()
    
    context['problems'] = problems_
    context.update(get_common_data())

    return render_template('problems.html', context=context)


@app.route('/edit_problem/<id_>/', methods=['GET', 'POST'])
def edit_problem(id_):
    problem_ = Problem.query.filter_by(id=id_).first()
    form = ProblemForm(
        title=problem_.title,
        level=problem_.level,
        text=problem_.text,
        category=problem_.category_id,
        answer=problem_.answer,
        knowledge=problem_.knowledge,
        advises=problem_.advises 
    )

    if request.method == 'POST':
        problem_.title = request.form['title']
        problem_.level = request.form['level']
        category_id = request.form.get('category', None)
        if not category_id:
            category = Category(title='Unknown category')
            category_id = category.id

        problem_.category_id = category_id
        problem_.text = request.form['text']
        problem_.knowledge = request.form.get('knowledge', None)
        problem_.answer = request.form.get('answer', None)
        # NotBug: i speccialy do not use here try except so user can find problem. it is prototype any way

        db.session.commit()
        return redirect( url_for('problem', id_=problem_.id) )
    context = {
        'form': form,
        'problem': problem_
    }
    context.update(get_common_data())

    return render_template('edit_problem.html', context=context)


@app.route('/create_problem/', methods=['GET', 'POST'])
def create_problem(id_=None):
    if id_:
        pass
    form = ProblemForm()
    if request.method == 'POST':
        title = request.form['title']
        level = request.form.get('level', '')
        category_id = request.form.get('category', None)
        if not category_id:
            category = Category(title='Unknown category')
            category_id = category.id
        text = request.form['text']
        knowledge = request.form.get('knowledge', None)
        answer = request.form.get('answer', None)
        # NotBug: i speccialy do not use here try except so user can find problem. we got here prototype any way
        problem_ = Problem(title=title, level=level, category_id=category_id, text=text, knowledge=knowledge, answer=answer)
        db.session.add(problem_)
        db.session.commit()
        return redirect( url_for('problem', id_=problem_.id))
    context = {
        'form': form
    }
    context.update(get_common_data())

    return render_template('create_problem.html', context=context)


@app.route('/problem/')
@app.route('/problem/<id_>')
@app.route('/problem/<id_>/')
def problem(id_=None):

    if request.args.get('random', None):
        problem_ = Problem.query.order_by(func.random()).first()
    else:
        problem_ = Problem.query.filter_by(id=id_).first()
    context = {
        'problem': problem_
    }
    context.update(get_common_data())

    return render_template('problem.html', context=context)


@app.route('/subscribe/')
def subscribe():
    return
