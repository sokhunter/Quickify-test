import unittest
from selenium.webdriver.support.ui import Select
from Quickify.helpers.project_helper import *

class Backlog_helper():
	def __init__(self, driver):
		self.driver = driver

	def open(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		projectHelper = Project_helper(self.driver)
		projectHelper.open()
		driver.find_element_by_xpath('//*[@id="accordionSidebar"]/li[1]/a').click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "Backlog")

	def save_uh(self, name, sprint, descripcion, user, priority):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		txtName = driver.find_element_by_id("Title")
		txtName.clear()
		txtName.send_keys(name)

		if(sprint != 0):
			txtSprint = driver.find_element_by_id("Sprint")
			txtSprint.clear()
			txtSprint.send_keys(sprint)

		txtDescription = driver.find_element_by_id("Description")
		txtDescription.clear()
		txtDescription.send_keys(descripcion)

		cbxUser = Select(driver.find_element_by_id("User_Id"))
		cbxUser.select_by_index(user)

		txtPriority = driver.find_element_by_id("Priority")
		txtPriority.clear()
		txtPriority.send_keys(priority)

	def save_task(self, name, date, description):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		txtName = driver.find_element_by_id("txt_Tasks_Title")
		txtName.clear()
		txtName.send_keys(name)

		txtDate = driver.find_element_by_id("txt_Tasks_IntendedDate")
		txtDate.clear()
		txtDate.send_keys(date)

		txtDescription = driver.find_element_by_id("txt_Tasks_Description")
		txtDescription.clear()
		txtDescription.send_keys(description)

		driver.find_element_by_id("btn_Tasks_Guardar").click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "Tareas segun Historia de Usuario")
