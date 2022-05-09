import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
  '''
  Test Class to test the behavior of the User class
  '''

  def setUp(self):
    '''
    Set up method that will run before every test.
    '''
    # self.new_user = User(1234, '')
    self.new_user = User(password='banana')

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password
    
  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('banana'))
