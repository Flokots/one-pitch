from flask import flash, render_template, redirect, url_for, abort, request
from flask_login import current_user, login_required

from . import main
from ..models import User, Pitch, Comment
from .forms import AddPitch, UpdateProfile, CommentForm
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

  mypitches = Pitch.query.filter_by(user_id = current_user.id).all()
  return render_template("profile/profile.html", user=user, mypitches=mypitches)


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

  return render_template('/index.html')    

@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():

  form = AddPitch()

  if form.validate_on_submit():
    user_id = current_user.id
    print(user_id)
    pitch = Pitch(name=form.name.data, description=form.description.data, category=form.category.data, user_id=user_id)
    db.session.add(pitch)
    db.session.commit()
    
    
    cname=form.category.data

    return redirect(url_for('main.pitch', cname=cname))
  return render_template('addpitch.html', pitch_form=form)




@main.route('/pitch/<int:pitch_id>/comment', methods=['GET', 'POST'])
@login_required
def new_comment(pitch_id):
  pitch_id = pitch_id
  form = CommentForm()

  if form.validate_on_submit():
    new_comment = Comment(name = form.name.data, pitch_id=pitch_id, user_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('.index'))

  return render_template('comment.html', form=form)
