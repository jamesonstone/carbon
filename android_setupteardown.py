'''
Android Setup and Teardown module
'''
import os
from time import sleep
from appium import webdriver

#DRIVER is the global variable
DRIVER = None

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def setUp():
    global DRIVER
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = PATH(
        '../../repo/android/app/build/apk/app-debug-unaligned.apk'
    )

    DRIVER = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def tearDown():       
    # end the session
    DRIVER.quit()