from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  '''
  User class to define User Objects
  '''
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pitches = db.relationship('Pitch', backref = 'pitcher', lazy='dynamic')
  comments = db.relationship('Comment', backref = 'commenter', lazy='dynamic')
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
    return f'{self.username}'


class Pitch(db.Model):
  '''
  Pitch class to define Pitch Objects
  '''
  __tablename__ = 'pitches'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text, nullable=False)
  category = db.Column(db.Text, nullable=False)
  posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __repr__(self):
    return f'{self.name}'


class Comment(db.Model):
  '''
  Comment class to define Comment Objects
  '''
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

  def __repr__(self):
    return f'{self.name}'
 