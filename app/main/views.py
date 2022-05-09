from flask import render_template, url_for
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


