from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

class user_vists_homepage(TestCase):
	def test_user_hits_url(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected = render_to_string('home.html')
		#decode converts bytes to python unicode string.
		self.assertEqual(response.content.decode(), expected)
		'''
		--> we shouldn't test constants. We checked for behaviour instead. 
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>To-Do Lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))'''
