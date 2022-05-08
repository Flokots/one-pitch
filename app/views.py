from flask import render_template
from app import app

@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''

  message = 'Hello World'
  return render_template('index.html', message=message)


@app.route('/categories')
def categories():
  '''
  View categories page function that returns the categories page and its data.
  '''
  title = "categories"
  return render_template('categories.html', title=title)


@app.route('/category/<int:id>')
def category(id):
  '''
  View category page function that returns the category details.
  '''


  return render_template('category.html', id=id)


