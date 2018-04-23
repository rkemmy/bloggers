from flask import redirect, url_for, jsonify
from flask_login import current_user, login_required
from flask import render_template
from . import main
from .forms import PostForm, CommentForm
from app.models import Post, Comment
from app import db
import pdb

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
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('posts/new.html', form=form)

# view individual posts & their comments
@main.route('/posts/<int:post_id>')
def view_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    # Get all comments associated with this post
    comments = Comment.query.filter_by(post_id=post_id).all()
    if post:
        return render_template('posts/show.html', post=post, comments=comments)
    return 'Post not found'

# TODO
# edit - edit, save and redirect to show page
@main.route('/posts/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    pass


    # title = request.args.get('title')
    # update_attributes = {title: title, body: body, timestamp: datetime.utcnow }
    # post = Post.update(update_attributes)
    # db.session.commit()
    # return redirect(url_for('main.view_post', post_id=post_id))
# delete - delete by id and redirect to all posts


@main.route('/posts/<int:post_id>/comments/', methods=['GET', 'POST'])
def create_comment(post_id):
    post = Post.query.filter_by(id=post_id).first()
    form = CommentForm()
    if form.validate_on_submit() and post is not None:
        comment = Comment(
            username    = form.username.data,
            description = form.description.data,
            post_id = post.id
        )
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.view_post', post_id=post.id))
    return render_template('posts/new_comment.html', form=form, post=post)
