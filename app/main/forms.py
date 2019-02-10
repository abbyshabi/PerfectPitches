from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
#from .models import User

class PostForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Publish')
    category = SelectField(
        "category",
        choices=[("pick-up", "pick-up"),("boring","boring"),("funny","funny"),("promotion","promotion"),("product","product"),("cheesy","cheesy"),("random","random")],validators = [Required()]
    )
   

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')