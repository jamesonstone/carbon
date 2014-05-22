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
    print 'setup module'
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

def setupLogin():
    return