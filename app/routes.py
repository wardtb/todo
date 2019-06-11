from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Tom'}
    items = [
        {
            'id': 1,
            'name': 'grocery store',
            'category': 'chores'
        },
        {
            'id': 2,
            'name': 'workout',
            'category': 'health'
        },
        {
            'id': 3,
            'name': 'run',
            'category': 'health'
        }

    ]
    return render_template('index.html', title='Home', user=user, items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
