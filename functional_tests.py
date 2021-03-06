from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class user_visits_website(unittest.TestCase):
	#special method that is started by the beginning of a test runner.	
	def setUp(self):
		self.browser = webdriver.Firefox()

	#special method that is fired by the end of a test runner.
	def tearDown(self):
		self.browser.quit()

	def test_user_notices_website_title(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')
	
		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		time.sleep(1)

		# She writes another to-do item and update the page. She sees all her input now.
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Fartaka Fartaka 3al Tabala W3al Saksaka')
		inputbox.send_keys(Keys.ENTER)

		time.sleep(1)

		# Page updated and she sees all her past input, a numerated list that contains all to-do items.
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn('2: Fartaka Fartaka 3al Tabala W3al Saksaka', [row.text for row in rows])

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)
		self.fail('finish the test!')

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main()


