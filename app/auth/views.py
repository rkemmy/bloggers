from .forms import LoginForm
from . import auth
from .models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
