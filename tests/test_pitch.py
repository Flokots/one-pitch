import unittest
from app.models import Pitch, User

class PitchModelTest(unittest.TestCase):
  '''
  Test Class to test the behavior of the Pitch Class
  '''

  def setUp(self):
    self.new_user = User(id=1, username='ndizi', email='ndizi@gmail.com', bio='hey world', profile_pic_path='/static/photos',password='banana')
    self.new_pitch = Pitch(id=1, name='Bizarre', description='Bizarre things happen in this world', category='Applications', upvotes=0, downvotes=0, user_id=1)

  def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
  def test_init(self):
    self.assertEqual(self.new_pitch.id, 1)
    self.assertEqual(self.new_pitch.name, 'Bizarre')
    self.assertEqual(self.new_pitch.description, 'Bizarre things happen in this world')
    self.assertEqual(self.new_pitch.category,'Applications')
    self.assertEqual(self.new_pitch.upvotes, 0)
    self.assertEqual(self.new_pitch.downvotes,0)
    self.assertEqual(self.new_pitch.user_id, 1)
  