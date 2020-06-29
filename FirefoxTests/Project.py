import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from Quickify.helpers.web_helper import *
from Quickify.helpers.auth_helper import *
from Quickify.helpers.project_helper import *

class Project(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\FirefoxTests\geckodriver-v0.26.0-win64\geckodriver.exe")
		webHelper = Web_helper(self.driver)
		webHelper.load()
		authHelper = Auth_helper(self.driver)
		authHelper.login('emylivaque@gmail.com', 'password')
		self.projectHelper = Project_helper(self.driver)

	def test_add(self):
		driver = self.driver
		driver.find_element_by_id("btn_Proyect_Crear").click()
		driver.implicitly_wait(5)
		self.projectHelper.save('test project', [('Andres Loa Puris', 'Analista'), ('Michell Reyes Cueva', 'Desarrollador')])

	def test_open(self):
		self.projectHelper.open()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='FirefoxTests/reports'))