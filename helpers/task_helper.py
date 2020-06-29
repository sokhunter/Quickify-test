import unittest
from selenium.webdriver.support.ui import Select

class Task_helper():
	def __init__(self, driver):
		self.driver = driver

	def list_tasks(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		driver.find_element_by_xpath('//*[@id="accordionSidebar"]/li[2]/a').click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "Tareas")
