from flask_login import current_user, login_required
from flask import render_template
from . import main

@main.route('/')
@login_required
def index():
    return render_template('index.html')

# @main.route()