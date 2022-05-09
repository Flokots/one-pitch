from . import db

class User(db.Model):
  '''
  User class to define User Objects
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))

  def __repr__(self):
    return f'User {self.username}'

class Comment:
  '''
  Comment class to define Comment Objects
  '''
  pass

class Pitch:
  '''
  Comment class to define Pitch Objects
  '''
  pass

class Category:
  '''
  Comment class to define Category Objects
  '''
  pass