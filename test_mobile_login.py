import os
from time import sleep
import android
import unittest 
from appium import webdriver


# def setUpModule():
#     android.setUp()

# def tearDownModule():
#     android.tearDown()



class TestMobileLogin(unittest.TestCase):

    def test_a_sign_button(self):
        DRIVER = android.setUp()

        # TODO: change this explicit wait
        #DRIVER.implicitly_wait(8)
        sleep(8)
        print '\nwait 8 seconds'
        
        el = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/login')
        self.assertIsNotNone(el)
        self.assertEquals('Sign in', el.text)
        print el.text()
        el.click()
        
        #enter bad credientals 
        #verify errors
        print 'entering bad email and password'
        email = android.DRIVER.find_element_by_id('com.voxy.news.debug:id/email')
        assertIsNotNone(email)
        email.send_keys('voxy@boxyroxy.com')

        password = androd.DRIVER.find_element_by_id('com.voxy.news.debug:id/password')
        assertIsNotNone(password)
        password.send_keys('wowowowowowo')
        DRIVER.implicitly_wait(8)

        signup = DRIVER.find_element_by_id('com.voxy.news.debug:id/signup')
        assertIsNotNone(signup)
        DRIVER.implicitly_wait(8)
        print signup.text()

        signup.click()
        DRIVER.implicitly_wait(8)

        alertmsg = DRIVER.find_element_by_id('android:id/alertTitle')
        assertIsNotNone(alertmsg)
        assertEquals(alertmsg.text, 'Email or password incorrect')



# main
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMobileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
