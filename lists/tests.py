from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.

class user_vists_homepage(TestCase):
	def test_user_hits_url(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
