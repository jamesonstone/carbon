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
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 , "startX": 698, "startY": 776,
		 "endX": 251, "endY": 779, "duration": 0.9256836 })
		sleep(5)








# main
if __name__ == '__main__':
    unittest.main(verbosity=2)