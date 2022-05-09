from flask import render_template, url_for
from flask_login import login_required

from . import main
from ..models import User, Comment

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''

  title = 'One Pitch'
  return render_template('index.html', title=title)


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


# @main.route('/pitch/<int:id>/comment/')