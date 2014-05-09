"""
Access iOS login page
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.join(os.path.dirname(__file__),
                           '/Users/Jameson/Library/Developer/Xcode/DerivedData/Voxy-duthalwrifywyzetfxjfrnnrehvp/Build/Products/Debug-iphonesimulator',
                           'Voxy.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app
            })

    def tearDown(self):
        self.driver.quit()

    def _populate(self):
        # populate text fields with two random numbers
        els = self.driver.find_elements_by_ios_uiautomation('elements()')

    def test_scroll(self):
        els = self.driver.find_elements_by_class_name('UIAButton')
        els[5].click()

        sleep(1)
        el = self.driver.find_element_by_name('OK')
        el.click()

        sleep(1)
        el = self.driver.find_element_by_xpath('//UIAMapView[1]')

        location = el.location
        self.driver.swipe(startx=location['x'], starty=location['y'], endx=0.5, endy=location['y'], duration=0.8)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    