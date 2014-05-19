import os
from time import sleep
import android
import unittest 
from appium import webdriver


class TestMobileLogin(unittest.TestCase):
    android.setUp()

    def test_a_sign_button(self):
        # TODO: change this explicit wait
        sleep(10)
        print '\nwait 8 seconds'
        el = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/login')
        android.assertIsNotNone(el)
        android.assertEquals('Sign in', el.text)
        print el.text()
        el.click()
        #enter bad credientals 
        #verify errors
        print 'entering bad email and password'
        email = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/email')
        android.assertIsNotNone(email)
        email.send_keys('voxy@boxyroxy.com')

        password = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/password')
        android.assertIsNotNone(password)
        password.send_keys('wowowowowowo')
        sleep(5)

        signup = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/signup')
        android.assertIsNotNone(signup)
        sleep(5)
        print signup.text()
        signup.click()
        #android.DRIVER.implicitly_wait(8)
        sleep(5)

        alertmsg = android.DRIVER.find_element_by_id('android:id/alertTitle')
        android.assertIsNotNone(alertmsg)
        android.assertEquals(alertmsg.text, 'Email or password incorrect')

    android.tearDown()



# main
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMobileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
