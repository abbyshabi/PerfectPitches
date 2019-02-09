from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post,Comment
from .forms import PostForm
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
# from ..email import mail_message
import datetime


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Pitches'
    form = PostForm()
    return render_template('index.html', form=form)

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


    
@main.route('/post/<category>')
def post(category):
    user=User.query.filter_by(id=id).first()
    post = None
   
    if category == 'all':
        post = Post.query.order_by(Post.date.desc())
    else :
        post = Post.query.filter_by(category = category).order_by(Post.time.desc()).all()

    return render_template('post.html', post = post ,title = category.upper())