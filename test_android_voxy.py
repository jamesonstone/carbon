import os
from time import sleep

import unittest 

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../repo/android/app/build/apk/app-debug-unaligned.apk'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        # TODO: change this implicity wait
        self.driver.implicitly_wait(8)
        el = self.driver.find_element_by_id('com.voxy.news.debug:id/login')
        self.assertIsNotNone(el)
        print el.text()
        el.click()



# main
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
