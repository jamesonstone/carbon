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

	def test_1_activity_workspace(self):
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/title'))
		android.driver.find_element_by_name('Navigate up').click()
		sleep(2)
		android.driver.find_element_by_xpath("//android.view.View[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[1]").click()
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/type'))
		sleep(2)
		android.driver.find_element_by_id('com.voxy.news.debug:id/entireRow').click()
		sleep(5)
		android.driver.find_element_by_id('com.voxy.news.debug:id/startActivity').click()
		sleep(2)
		android.driver.find_element_by_xpath('//android.view.View[1]/android.widget.LinearLayout[1]').click()
		sleep(2)




# main
if __name__ == '__main__':
    unittest.main(verbosity=2)
