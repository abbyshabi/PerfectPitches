from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password) :
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    date = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String)
    comments = db.relationship("Comment", backref = "comment", lazy = "dynamic")

    def save_post(self):
        '''
        Function to save a new pitch
        '''
        db.session.add(self)
        db.session.commit()

    def get_post_comments(self):
        post = Post.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(id = post.id)
        
        return comments
    

class Comment(db.Model):
     
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()   

        
        
    


