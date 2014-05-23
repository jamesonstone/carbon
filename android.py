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
    driver.implicitly_wait(8)
    login_button = driver.find_element_by_id('com.voxy.news.debug:id/login')
    login_button.click()
    email = driver.find_element_by_id('com.voxy.news.debug:id/email')
    email.send_keys('mobiletesting@voxy.com')
    password = driver.find_element_by_id('com.voxy.news.debug:id/password')
    password.send_keys('things')

    signup = driver.find_element_by_id('com.voxy.news.debug:id/signup')
    signup.click()
    sleep(5)


