import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("..")
from Quickify.helpers.web_helper import *
from Quickify.helpers.auth_helper import *
from Quickify.helpers.backlog_helper import *
from Quickify.helpers.task_helper import *

class Task(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Edge(executable_path=r"C:\Users\emyli\Desktop\Stefany\Cursos\Python\selenium\AlquilerEquipos\EdgeTests\edgedriver_win64\msedgedriver.exe")
		webHelper = Web_helper(self.driver)
		webHelper.load()
		authHelper = Auth_helper(self.driver)
		authHelper.login('emylivaque@gmail.com', 'password')
		self.backlogHelper = Backlog_helper(self.driver)
		self.backlogHelper.open()
		self.driver.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr/td[6]/a').click()
		self.driver.implicitly_wait(5)

	def test_list_us_tasks(self):
		driver = self.driver
		taskHelper = Task_helper(self.driver)
		taskHelper.list_tasks()
		
	def test_add_user_story_task(self):
		driver = self.driver
		driver.find_element_by_id("btn_Tasks_Crear").click()
		driver.implicitly_wait(5)
		self.backlogHelper.save_task('test task us', '002020-12-09T18:11:00', 'test description')
		
	def test_edit_user_story_task(self):
		driver = self.driver
		driver.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr[2]/td[1]/a[1]').click()
		driver.implicitly_wait(5)
		self.backlogHelper.save_task('test edit task us', '002021-12-09T18:11:00', 'test edit description')
		
	def test_delete_user_story_task(self):
		driver = self.driver
		driver.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr[2]/td[1]/a[2]').click()
		driver.implicitly_wait(5)
		
	def test_finish_task(self):
		driver = self.driver
		taskHelper = Task_helper(self.driver)
		taskHelper.list_tasks()
		driver.find_element_by_id("btn_Tasks_Finalizar").click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Tareas")
		
	def test_restart_task(self):
		driver = self.driver
		taskHelper = Task_helper(self.driver)
		taskHelper.list_tasks()
		driver.find_element_by_id("btn_Tasks_Restaurar").click()
		driver.implicitly_wait(5)
		self.assertEqual(driver.title, "Tareas")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='EdgeTests/reports'))