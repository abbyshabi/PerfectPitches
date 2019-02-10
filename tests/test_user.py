import unittest
from app.models import User
from app import db


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(1,'Python','abc@gmail.com',2,'abcd','abc.jpg','abcd')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
