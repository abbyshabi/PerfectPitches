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
