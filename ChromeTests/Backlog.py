import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from Quickify.helpers.auth_helper import *
from Quickify.helpers.backlog_helper import *

class Backlog(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\ChromeTests\chromedriver_win32\chromedriver.exe")
		self.driver.get("https://quickify.azurewebsites.net/Auth/login")
		self.driver.implicitly_wait(5)
		authHelper = Auth_helper(self.driver)
		authHelper.login('emylivaque@gmail.com', 'password')
		self.backlogHelper = Backlog_helper(self.driver)
		self.backlogHelper.open()

	def test_add_user_story(self):
		driver = self.driver
		driver.find_element_by_id("btn_HU_Crear").click()
		driver.implicitly_wait(5)
		self.backlogHelper.save_uh('HU test', 3, 'test', 1, 2)
		driver.find_element_by_id("btn_HU_guardar").click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Backlog")

	def test_edit_user_story(self):
		driver = self.driver
		driver.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr/th/a[1]').click()
		driver.implicitly_wait(5)
		self.backlogHelper.save_uh('HU test edit', 2, 'test', 1, 2)
		driver.find_element_by_xpath('//*[@id="content"]/div/form/div/div[4]/div/input').click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Backlog")

	def test_delete_user_story(self):
		driver = self.driver
		driver.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr/th/a[2]').click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Backlog")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='EdgeTests/reports'))