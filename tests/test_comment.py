import unittest
from app.models import Comment,User
from flask_login import current_user
from app import db


class TestComment(unittest.TestCase):

        def setUp(self):
                self.post_Fly = Post(title = 'James',body = 'potato', id = '1')
                self.new_comment = Comment(body = 'good')


        def tearDown(self):
                Post.query.delete()
                Comment.query.delete()

        def test_check_instance_variables(self):
                self.assertEquals(self.new_comment.post_id,12345)
                self.assertEquals(self.new_comment.post_title,'Review for movies')
                self.assertEquals(self.new_comment.post_comment,'This movie is the best thing since sliced bread')
                self.assertEquals(self.new_comment.user,self.user_James)

        def test_save_comment(self):
                self.new_comment.save_comment()
                self.assertTrue(len(Comment.query.all())>0)

        def test_get_comment_by_id(self):

                self.new_comment.save_comment()
                got_comments = Comment.get_comment(12345)
                self.assertTrue(len(got_comments) == 1)