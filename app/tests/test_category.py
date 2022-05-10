import unittest
from app.models import Category

class CategoryModelTest(unittest.TestCase):
  def setUp(self):
    self.new_category = Category(name = 'banana')


  def test_category(self):
    self.assertTrue(self.new_category.name is not None)

