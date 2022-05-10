from flask import render_template,redirect, url_for, abort
from flask_login import login_required

from . import main
from ..models import User, Comment
from .forms import UpdateProfile
from .. import db

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



@main.route('/categories')
def categories():
  '''
  View categories page function that returns the categories page and its data.
  '''
  title = "Categories"
  return render_template(url_for('categories.html'), title=title)


@main.route('/category/<int:id>')
def category(id):
  '''
  View category page function that returns the category details.
  '''


  return render_template(url_for('category.html'), id=id)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def pitch(id):
  '''
  View pitch page function that returns the pitch details.
  '''

  return render_template(url_for('pitch.html'), id=id)


