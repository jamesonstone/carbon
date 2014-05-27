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
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 , "startX": 693,
		 "startY": 818, "endX": 224, "endY": 833, "duration": 1.216719 })
		sleep(3)
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 ,
		 "startX": 718, "startY": 778, "endX": 239, "endY": 781, "duration": 1.201836 })
		sleep(3)
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 ,
		 "startX": 118, "startY": 820, "endX": 531, "endY": 824, "duration": 1.307949 })
		sleep(3)
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/snapshot'))
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/currentLevel'))








# main
if __name__ == '__main__':
    unittest.main(verbosity=2)