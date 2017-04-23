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
		#render_to_string takes a dictionary as a second parameter to map the variables values.
		expected = render_to_string('home.html', request=request)

		#decode converts bytes to python unicode string.
		self.assertEqual(response.content.decode(), expected)

		'''
		--> we shouldn't test constants. We checked for behaviour instead. 
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>To-Do Lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))'''

	def test_home_page_save_POST_request(self):
		#Setup test
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		#Exercise test
		response = home_page(request)

		#Assert test
		self.assertIn('A new list item', response.content.decode())

	