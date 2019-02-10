import unittest
from app.models import Comment
from app import db


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Abby = User(username = 'Abby' ,password = 'potatoe', email='potatoe@hmail.com')
        self.new_comment = Comment(1,'Python','abc@gmailcom',2,3)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def tearDown(self):
        User.query.delete()
        Role.query.delete()
        Comment.query.delete()
        Post.query.delete()