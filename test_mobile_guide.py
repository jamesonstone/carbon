import os
from time import sleep
import unittest 
from appium import webdriver
import android



def setUpModule():
    android.setUpLogin()

def tearDownModule():
    android.tearDown()


class TestMobileGuide(unittest.TestCase):

	def test_1_guide_items(self):
		android.driver.implicitly_wait(10)
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/title'))
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/goalsTitle'))












# main
if __name__ == '__main__':
    unittest.main(verbosity=2)