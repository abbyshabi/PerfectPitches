import unittest
from app.models import Role
from app import db


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_role = Role(1,'Python','abc@gmailcom')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_role,Role))
