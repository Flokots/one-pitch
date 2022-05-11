from flask import flash, render_template, redirect, url_for, abort, request
from flask_login import login_required

from . import main
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, AddPitch
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


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
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


@main.route('/pitches/<cname>', methods=["GET", "POST"])
def pitch(cname):
  '''
  View root page function that returns the pitches page and its data
  '''
  pitches = Pitch.query.all()

  if cname == 'pickuplines':
    pickuplines = Pitch.query.filter_by(category='Pick Up Lines')
    return render_template('pitches/pickuplines.html', pickuplines=pickuplines)
  if cname == 'business':
    business = Pitch.query.filter_by(category="Business")
    return render_template('pitches/business.html', business=business)
  if cname == 'designs':
    designs = Pitch.query.filter_by(category="Designs")
    return render_template('pitches/designs.html', designs=designs)
  if cname == 'interview':
    interviews = Pitch.query.filter_by(category="Interview")
    return render_template('pitches/interview.html', interviews=interviews)
  if cname == 'products':
    products = Pitch.query.filter_by(category="Product")
    return render_template('pitches/product.html', products=products)
  if cname == 'applications':
    applications = Pitch.query.filter_by(category="Applications")
    return render_template('pitches/applications.html', applications=applications)


  return render_template('pitches.html', pitches=pitches, applications=applications, pickuplines=pickuplines, business=business, designs=designs, interviews=interviews, products=products)


@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():

  form = AddPitch()

  if form.validate_on_submit():
    pitch = Pitch(name=form.name.data, description=form.description.data, category=form.category.data)
    db.session.add(pitch)
    db.session.commit()

    return redirect(url_for('main.pitch'))
  return render_template('addpitch.html', pitch_form=form)

