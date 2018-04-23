from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, TextAreaField
from wtforms.validators import Required, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required(), Length(min=4, max=50)])
    body = TextAreaField('Body', validators=[Required(),Length(min=1, max=400)])
    submit = SubmitField('Create Post')


class CommentForm(FlaskForm):
    username = StringField('Name', validators=[Required()])
    description = TextAreaField('Comment', validators=[Required(), Length(min=1, max=400)])
    submit = SubmitField('Submit')
