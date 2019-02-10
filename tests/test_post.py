import unittest
from app.models import Post
from app import db


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1,'Python','abc@gmailcom',2/10/12,'abcd','abcjpg','abcd')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
