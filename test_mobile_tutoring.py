import os
from time import sleep
import unittest 
from appium import webdriver
import android



def setUpModule():
    android.setUpLogin()

def tearDownModule():
    android.tearDown()


class TestMobileExplore(unittest.TestCase):

	def test_1_tutoring(self):
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/title'))
		android.driver.find_element_by_name('Navigate up').click()
		sleep(2)
		# in the side menu, select tutoring
		android.driver.find_element_by_xpath("//android.view.View[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.TextView[1]").click()
		self.assertIsNotNone(android.driver.find_element_by_xpath('//android.view.View[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.TextView[1]'))
		sleep(2)
		# click the pop up 'Schedule a Session'
		self.assertIsNotNone(android.driver.find_element_by_xpath("//android.widget.Button[1]"))
		android.driver.find_element_by_xpath("//android.widget.Button[1]").click()
		sleep(2)
		# click 'continue' button on FT New Session
		self.assertIsNotNone(android.driver.find_element_by_xpath('//android.view.View[2]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.Button[1]'))
		android.drive.find_element_by_xpath("//android.view.View[2]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.Button[1]").click()
		sleep(2)




# main
if __name__ == '__main__':
    unittest.main(verbosity=2)
