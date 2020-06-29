import unittest

class Auth_helper():
	def __init__(self, driver):
		self.driver = driver
	
	def login(self, user, password):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_id("txt_Auth_Email").send_keys(user)
		driver.find_element_by_id("txt_Auth_Password").send_keys(password)
		driver.find_element_by_id("btn_Auth_Login").click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "QUICKIFY - Proyectos")