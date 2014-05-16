import os
from time import sleep

import unittest 

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

driver = None

def setUp():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
            '../../repo/android/app/build/apk/app-debug-unaligned.apk'
        )
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def tearDown():
    # end the session
    driver.quit()




class TestMobileLogin(  unittest.TestCase):
#     def setUp(self):
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '4.2'
#     desired_caps['deviceName'] = 'Android Emulator'
#     desired_caps['app'] = PATH(
#             '../../repo/android/app/build/apk/app-debug-unaligned.apk'
#         )
#     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# def tearDown(self):
#     # end the session
#     self.driver.quit()

    def test_a_sign_button(self):
        # TODO: change this explicit wait
        self.driver.implicitly_wait(8)
        print '\nwait 8 seconds'
        el = self.driver.find_element_by_id('com.voxy.news.debug:id/login')
        self.assertIsNotNone(el)
        self.assertEquals('Sign in', el.text)
        print el.text
        el.click()
        #enter bad credientals 
        #verify errors
        print 'entering bad email and password'
        email = self.driver.find_element_by_id('com.voxy.news.debug:id/email')
        self.assertIsNotNone(email)
        email.send_keys('voxy@boxyroxy.com')

        password = self.driver.find_element_by_id('com.voxy.news.debug:id/password')
        self.assertIsNotNone(password)
        password.send_keys('wowowowowowo')
        self.driver.implicitly_wait(5)

        signup = self.driver.find_element_by_id('com.voxy.news.debug:id/signup')
        self.assertIsNotNone(signup)
        self.driver.implicitly_wait(5)
        print signup.text
        signup.click()
        self.driver.implicitly_wait(8)

        alertmsg = self.driver.find_element_by_id('android:id/alertTitle')
        self.assertIsNotNone(alertmsg)
        self.assertEquals(alertmsg.text, 'Email or password incorrect')




# main
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMobileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
