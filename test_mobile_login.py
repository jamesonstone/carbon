import os
from time import sleep
import unittest 
from appium import webdriver
import android



def setUpModule():
    android.setUp()

def tearDownModule():
    android.tearDown()


class TestMobileLogin(unittest.TestCase):

    def test_1_login_button(self):
        # TODO: change this explicit wait
        android.driver.implicitly_wait(8)
        login_button = android.driver.find_element_by_id('com.voxy.news.debug:id/login')
        self.assertIsNotNone(login_button)
        login_button.click()

    def test_2_login_bad_user(self):
        email = android.driver.find_element_by_id('com.voxy.news.debug:id/email')
        self.assertIsNotNone(email)
        email.send_keys('voxy@boxyroxy.com')

        password = android.driver.find_element_by_id('com.voxy.news.debug:id/password')
        self.assertIsNotNone(password)
        password.send_keys('wowowowowowo')

        signup = android.driver.find_element_by_id('com.voxy.news.debug:id/signup')
        self.assertIsNotNone(signup)
        signup.click()
        android.driver.implicitly_wait(5)

        alertmsg = android.driver.find_element_by_id('android:id/alertTitle')
        self.assertIsNotNone(alertmsg)

        android.driver.find_element_by_id('android:id/button1').click()

        android.driver.back()        

        android.driver.find_element_by_id('com.voxy.news.debug:id/register').click()

    def test_3_register_bad_user(self):
        return



# main
if __name__ == '__main__':
    unittest.main(verbosity=2)





















    #enter bad credientals 
        # #verify errors
        # print 'entering bad email and password'
        # email = android.driver.find_element_by_id('com.voxy.news.debug:id/email')
        # assertIsNotNone(email)
        # email.send_keys('voxy@boxyroxy.com')

        # password = androd.driver.find_element_by_id('com.voxy.news.debug:id/password')
        # assertIsNotNone(password)
        # password.send_keys('wowowowowowo')
        # driver.implicitly_wait(8)

        # signup = driver.find_element_by_id('com.voxy.news.debug:id/signup')
        # assertIsNotNone(signup)
        # driver.implicitly_wait(8)
        # print signup.text()

        # signup.click()
        # driver.implicitly_wait(8)

        # alertmsg = driver.find_element_by_id('android:id/alertTitle')
        # assertIsNotNone(alertmsg)
        # assertEquals(alertmsg.text, 'Email or password incorrect')
