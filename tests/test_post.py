import unittest
from app.models import Post,User
from flask_login import current_user
from app import db


class TestPost(unittest.TestCase):

        def setUp(self):
                self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
                self.new_post= Post(id=12345,title='Title for pitches',comments='This movie is the best thing since sliced bread',author_id =1)


        def tearDown(self):
                Post.query.delete()
                User.query.delete()
                Comment.query.delete()

       
        def test_save_post(self):
                self.new_post.save_post()
                self.assertTrue(len(Post.query.all())>0)

        def test_get_oist_by_id(self):

                self.new_post.save_post()
                got_post = Post.get_posts(1)
                self.assertTrue(len(got_posts) == 1)