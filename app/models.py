from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique=True, index= True)
    username = db.Column(db.String(60), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy='dynamic')


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique=True)
    body = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'comment', lazy='dynamic')

    # parse timestamp
    @staticmethod
    def time_parser(time_str):
        # TODO
        # use hours ago if less than 24 hours $ days afterwards
        new_date = time_str.date()
        return new_date

    def __repr__(self):
        return '<Posts {}>'.format(self.title)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(400))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return  '<Comments {}>'.format(self.description)
