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
        android.driver.implicitly_wait(5)
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

    def test_3_check_reg_button(self):
        android.driver.implicitly_wait(3)        
        reg_button = android.driver.find_element_by_id('com.voxy.news.debug:id/register')
        self.assertIsNotNone(reg_button)
        reg_button.click()
        android.driver.implicitly_wait(3)

    def test_4_check_reg_form(self):
        fname = android.driver.find_element_by_id('com.voxy.news.debug:id/name')
        self.assertIsNotNone(fname)
        email = android.driver.find_element_by_id('com.voxy.news.debug:id/email')
        self.assertIsNotNone(email)
        password = android.driver.find_element_by_id('com.voxy.news.debug:id/password')
        self.assertIsNotNone(password)
        org = android.driver.find_element_by_id('com.voxy.news.debug:id/redemptionQuestion')
        self.assertIsNotNone(org)
        reg_button = android.driver.find_element_by_id('com.voxy.news.debug:id/signup')
        self.assertIsNotNone(reg_button)
        facebook = android.driver.find_element_by_id('com.voxy.news.debug:id/login_button')
        self.assertIsNotNone(facebook)
        google = android.driver.find_element_by_id('com.voxy.news.debug:id/sign_in_button')
        self.assertIsNotNone(google)
        android.driver.implicitly_wait(5)


    def test_4_register_bad_user(self):
        android.driver.find_element_by_id('com.voxy.news.debug:id/name').send_keys('asdfjadkjfadsljdfsdfj')
        android.driver.find_element_by_id('com.voxy.news.debug:id/email').send_keys('asdkjfsdlkjfskldfsdufosdiufwe098098ew0823023809asdfasdfsdfsdfsd324238@voxy.com')
        android.driver.find_element_by_id('com.voxy.news.debug:id/password').send_keys('asjhdfajhsdflhajkdshfalshdflkjahsdlfkjhaskldhfhajsdfjaahdsfjhasdljhflasdkj2372938423784hjshdfakshfsjf')
        android.driver.find_element_by_id('com.voxy.news.debug:id/signup').click()
        android.driver.implicitly_wait(5)
        ok_button = android.driver.find_element_by_id('android:id/button1')
        self.assertIsNotNone(ok_button)
        ok_button.click()
        android.driver.back()


# main
if __name__ == '__main__':
    unittest.main(verbosity=2)
