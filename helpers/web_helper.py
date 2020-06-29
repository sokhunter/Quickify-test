import unittest

class Web_helper():
	def __init__(self, driver):
		self.driver = driver
	
	def load(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		self.driver.get("https://webappquickify.azurewebsites.net")
		self.driver.implicitly_wait(5)