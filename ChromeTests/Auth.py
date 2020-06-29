import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from Quickify.helpers.web_helper import *
from Quickify.helpers.auth_helper import *

class Auth(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\ChromeTests\chromedriver_win32\chromedriver.exe")
		webHelper = Web_helper(self.driver)
		webHelper.load()

	def test_signup(self):
		driver = self.driver
		driver.find_element_by_id("btn_Auth_SignUp").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("Name").send_keys("Stefany Livaque")
		driver.find_element_by_id("txt_Auth_Email").send_keys("admin")
		driver.find_element_by_id("txt_Auth_Password").send_keys("admin")
		driver.find_element_by_id("btn_Auth_Registrar").click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "SI657 - QUICKIFY")

	def test_login(self):
		authHelper = Auth_helper(self.driver)
		authHelper.login('emylivaque@gmail.com', 'password')

	def test_logout(self):
		driver = self.driver
		authHelper = Auth_helper(driver)
		authHelper.login('emylivaque@gmail.com', 'password')
		driver.find_element_by_id("userDropdown").click()
		driver.find_element_by_id("btn_Logout").click()
		self.assertEqual(driver.title, "SI657 - QUICKIFY")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='ChromeTests/reports'))