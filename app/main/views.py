from flask import redirect, url_for, jsonify
from flask_login import current_user, login_required
from flask import render_template
from . import main
from .forms import PostForm
from app.models import Post
from app import db

@main.route('/')
@login_required
def index():
    # get all posts in a chronological order
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)

# Create & View all posts
@main.route('/posts', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            body = form.body.data,
            author = current_user
        )

        # db.create_all()
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('posts/new.html', form=form)

# view individual posts
@main.route('/posts/<int:post_id>')
def view_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        return render_template('posts/show.html', post=post)
    return 'Post not found'

# TODO
# edit - edit, save and redirect to show page
# delete - delete by id and redirect to all posts
