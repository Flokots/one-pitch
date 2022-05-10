from flask import render_template,redirect, url_for, abort, request
from flask_login import login_required

from . import main
from ..models import User, Category, Pitch, Comment
from .forms import UpdateProfile
from .. import db, photos

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''

  title = 'One Pitch'
  return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()
  
  if user is None:
    abort(404)
  
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('main.profile', uname=user.username))
  return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()

  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  
  return redirect(url_for('main.profile', uname=uname))

@main.route('/category/<int:id>')
def category(id):
  '''
  View root page function that returns the categories page and its data.
  '''
  
  category = Category.query.filter_by(id=id).first()
  return render_template('category.html', category=category)


@main.route('/pitches/<int:id>', methods = ["GET","POST"])
def pitches(id):
  '''
  View root page function that returns the pitches page and its data
  '''
  return render_template('pitches.html', id=id)
