from flask import render_template

from app import APP


@APP.route('/')
@APP.route('/index')
def index():
    user = {'username': 'Florent'}
    return render_template('index.html', title='The AI Engineer', user=user)
