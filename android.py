'''
Android Setup and Teardown module
'''
import os
from time import sleep
import unittest
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def setUp():
    print 'setup'
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../../repo/android/app/build/apk/app-debug-unaligned.apk'
    )
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def tearDown():
    print 'teardown'
    # end the session
    driver.quit()

def setUpLogin():
    print 'setup and login module'
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../../repo/android/app/build/apk/app-debug-unaligned.apk'
    )
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    #login user
    android.driver.implicitly_wait(8)
    login_button = android.driver.find_element_by_id('com.voxy.news.debug:id/login')
    login_button.click()
    email = android.driver.find_element_by_id('com.voxy.news.debug:id/email')
    email.send_keys('jameson@stone.tc')
    password = android.driver.find_element_by_id('com.voxy.news.debug:id/password')
    password.send_keys('things')

    signup = android.driver.find_element_by_id('com.voxy.news.debug:id/signup')
    signup.click()
    android.driver.implicitly_wait(8)


