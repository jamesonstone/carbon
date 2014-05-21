import os
from time import sleep
import android
import unittest 
from appium import webdriver

global login_button


class TestMobileLogin(unittest.TestCase):
    def setUp(self):
        self.driver = android.setUp()

    def tearDown(self):
        android.tearDown()

    def test_login(self):
        # TODO: change this implicity wait
        self.driver.implicitly_wait(8)
        login_button = self.driver.find_element_by_id('com.voxy.news.debug:id/login')
        self.assertIsNotNone(login_button)

    def test_login_button(self):
        login_button = self.driver.find_element_by_id('com.voxy.news.debug:id/login')
        login_button.click()




# main
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMobileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)





















    #enter bad credientals 
        # #verify errors
        # print 'entering bad email and password'
        # email = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/email')
        # assertIsNotNone(email)
        # email.send_keys('voxy@boxyroxy.com')

        # password = androd.DRIVER.find_element_by_id('com.voxy.news.debug:id/password')
        # assertIsNotNone(password)
        # password.send_keys('wowowowowowo')
        # DRIVER.implicitly_wait(8)

        # signup = DRIVER.find_element_by_id('com.voxy.news.debug:id/signup')
        # assertIsNotNone(signup)
        # DRIVER.implicitly_wait(8)
        # print signup.text()

        # signup.click()
        # DRIVER.implicitly_wait(8)

        # alertmsg = DRIVER.find_element_by_id('android:id/alertTitle')
        # assertIsNotNone(alertmsg)
        # assertEquals(alertmsg.text, 'Email or password incorrect')
