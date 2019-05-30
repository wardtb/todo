from flask import render_template
from app import app

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
