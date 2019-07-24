# -*- coding: utf-8 -*-
from flask import render_template
from app import app

from app import app, db
from models import Category, Problem
from flask import Flask, Response

import os


def get_common_data():

    problems_ = Problem.query

    data = {
        'categories': Category.query.all(),
        'all_problems_qty': len(problems_.all()),
        'junior_problems_qty': len(problems_.filter_by(level=1).all()),
        'middle_problems_qty': len(problems_.filter_by(level=2).all()),
        'senior_problems_qty': len(problems_.filter_by(level=3).all()),
        'legend_problems_qty': len(problems_.filter_by(level=4).all()),
        'insane_problems_qty': len(problems_.filter(Problem.level==4).all())
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
        problems_ = Problem.query.filter_by(category_id=category.id).all()

        context['category'] = category
    else:
        problems_ = Problem.query.all()
    
    context['problems'] = problems_
    context.update(get_common_data())

    return render_template('problems.html', context=context)


@app.route('/create_problem/')
def create_problem(slug=None):
    # result = Result(
    #     url=url,
    #     result_all=raw_word_count,
    #     result_no_stop_words=no_stop_words_count
    # )
    # db.session.add(result)
    # db.session.commit()

    context = {
        'slug': slug
    }
    context.update(get_common_data())

    return render_template('create_problem.html', context=context)


@app.route('/problem/<id>')
@app.route('/problem/<id>/')
def problem(id):
    problem_ = Problem.query.filter_by(id=id).first()
    context = {
        'problem': problem_
    }
    context.update(get_common_data())

    return render_template('problem.html', context=context)


@app.route('/subscribe/')
def subscribe():
    return


