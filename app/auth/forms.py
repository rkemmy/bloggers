from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField,StringField,PasswordField,TextAreaField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required])
    password = PasswordField('Password', validators=[Required])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

