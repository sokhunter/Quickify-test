import unittest
from selenium.webdriver.support.ui import Select

class Project_helper():
	def __init__(self, driver):
		self.driver = driver

	def open(self):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver
		
		driver.find_element_by_id('btn_Proyect_Open').click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "Kanban")

	def save(self, name, members):
		my_assertion = unittest.TestCase('__init__')
		driver = self.driver

		txtName = driver.find_element_by_id("Proyecto_txt_Nombre")
		txtName.clear()
		txtName.send_keys(name)

		cbxName = Select(driver.find_element_by_id("Proyecto_ddl_Desarrollador"))
		cbxRol = Select(driver.find_element_by_id("Proyecto_ddl_Role"))
		for member in members:
			cbxName.select_by_value(member[0])
			cbxRol.select_by_value(member[1])
			driver.find_element_by_id("addToList").click()

		driver.find_element_by_id("Alquiler_btn_Guardar").click()
		driver.implicitly_wait(5)
		my_assertion.assertEqual(driver.title, "QUICKIFY - Proyectos")

		