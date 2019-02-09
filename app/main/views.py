from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post
from .forms import PostForm
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
# from ..email import mail_message
import datetime


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Blogger'

    form = PostForm()

    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        post.save_post()
        return redirect(url_for('.index'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('index.html', form=form, posts=posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html')

@main.route('/pitch/<int:id>')
def pitch(id):
    post = Post.query.get_or_404(id)
    return render_template('posts.html', posts=[post])