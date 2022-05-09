from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model):
  '''
  User class to define User Objects
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

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