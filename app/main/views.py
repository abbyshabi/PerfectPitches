from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post,Comment
from .forms import PostForm,CommentForm,UpdateProfile
from .. import db,photos
from flask_login import login_user, logout_user, login_required, current_user
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
    
    posts= None
    if category == 'all':
        posts = Post.query.order_by(Post.date.desc())
    else :
        posts = Post.query.filter_by(category = category).order_by(Post.date.desc()).all()

    return render_template('post.html', posts = posts ,title = category.upper())

@main.route('/new/post/<uname>', methods = ['GET','POST'])
@login_required
def new_post(uname):
    form = PostForm()
    title = 'Express yourself'
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
      
    if form.validate_on_submit():
        title = form.title.data
        body = form.post.data
        category = form.category.data 
        dateNow = datetime.datetime.now()
        date = str(dateNow)
    

        add_post = Post(title = title,body=body,category=category,date=date)
        add_post.save_post()
        posts = Post.query.all()
        return redirect(url_for('main.post',category = category ))
    return render_template('new_post.html', form = form, title =title)

 

@main.route('/post/<post_id>/add/comment', methods = ['GET','POST'])
@login_required
def comment(post_id):
   
    post = Post.query.filter_by(id = post_id).first()
    form = CommentForm()
 
    if form.validate_on_submit():
        body = form.body.data
      
        new_comment = Comment(body=body)
        new_comment.save_comment()
        
        return redirect(url_for("main.show_comments",post_id = post_id))
    return render_template("comment.html", form = form, post = post)

@main.route('/<post_id>/comments')
@login_required
def show_comments(post_id):
    
    post = Post.query.filter_by(id = post_id).first()
    
    comments = post.get_post_comments()

    return render_template('show_comments.html',comments= comments,post=post)


       