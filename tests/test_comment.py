import unittest

from flask import session
from app import db
from app.models import Comment, User, Pitch

class CommentModelTest(unittest.TestCase):
  '''
  Test Class to test the behavior of the Comment class
  '''
  def setUp(self):
    self.new_comment = Comment(id=1550, name='Worldy', user_id=1, pitch_id=1)
    self.new_user = User(id=1, username='ndizi', email='ndizi@gmail.com', bio='hey world', profile_pic_path='/static/photos',password='banana')
    self.new_pitch = Pitch(id=1, name='Bizarre', description='Bizarre things happen in this world', category='Applications', upvotes=0, downvotes=0, user_id=1)


  def tearDown(self):
    Comment.query.delete()
    Pitch.query.delete()
    User.query.delete()
    db.session.remove()
  
  def test_init(self):
    self.assertEquals(self.new_comment.id, 1550)
    self.assertEqual(self.new_comment.name, 'Worldy')
    self.assertEqual(self.new_comment.user_id, 1)
    self.assertEqual(self.new_comment.pitch_id, 1)

    self.assertEqual(self.new_user.id, 1)
    self.assertEqual(self.new_user.username, 'ndizi')
    self.assertEqual(self.new_user.email, 'ndizi@gmail.com')
    self.assertEqual(self.new_user.bio, 'hey world')
    self.assertEqual(self.new_user.profile_pic_path, '/static/photos' )

    self.assertEqual(self.new_pitch.id, 1)
    self.assertEqual(self.new_pitch.name, 'Bizarre')
    self.assertEqual(self.new_pitch.description, 'Bizarre things happen in this world')
    self.assertEqual(self.new_pitch.category,'Applications')
    self.assertEqual(self.new_pitch.upvotes, 0)
    self.assertEqual(self.new_pitch.downvotes,0)
    self.assertEqual(self.new_pitch.user_id, 1)
    

  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all() > 0))

  def test_get_comment_by_id(self):
    self.new_comment.save_comment()
    got_comments = Comment.get_comment(1550)
    self.assertTrue(len(got_comments) == 1)
    print(len(got_comments))