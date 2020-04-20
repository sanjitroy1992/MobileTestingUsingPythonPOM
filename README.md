# Mobile Testing Using Python POM
The project is build using python Appium client for mobile testing using an open-source testing solution. 

Page Object Model (POM) is a design pattern, popularly used in test automation that creates Object Repository for web UI elements. The advantage of the model is that it reduces code duplication and improves test maintenance.

In this tutorial we are going to learn how to create a simple logoin Test to automate a scenario using POM.

Step by Step:

We will do this hands-on:

Create a simple login test. Use python selenium webdriver to create a simple login test.
Implement unit testing. In order to conver a test to a unittest do the following steps.
import unittest
create a class with as below passing unittest Testcases module ->class LoginPage(unittest.Testcase)
create a setUpClass method which will be initialized at the beginning of tests. One thing to remember when you are usign a class function always provide the anotation at classmethod. @classmethod def setUp(self):
create a tearDownClass method which will be called at the end of all the tests. like setUpClass method provide the anotation at classmethod for tearDownClass. @classmethod def tearDown(self):
To create test cases make sure to name it starting with 'test'. As an example: test_login_page(self): 'test' is to tell unittest that it is a test case.
Implement Page Object Model
Separate test scripts and objects
Create a separate class for Locators
Run from command line
Add HTML Reports
Command to execute the tests: Since our python modeles are under venv folder so we need to first set the PythonPath followed by running the test with the below command.
set PYTHONPATH=./venv/Lib/site-packages;
python TestCases\AmazonSearch.py -v


PREREQUISITES
 - Java installed on system
 - JAVA_HOME is set in environment variables
 command to check : java -version
 - An android mobile device
 - Connecting cable
 - 200 MB to 1 GB of free space

Step 1 : Download SDK tools
 https://developer.android.com/studio
----------------------------------------------------------------------------------
Step 2 : Unzip folder & Extract platform tools
----------------------------------------------------------------------------------
Step 3 : Set environment variables
 ANDROID_HOME = location of sdk folder
 Path : append path of platform_tools folder
----------------------------------------------------------------------------------
Step 4 : Check command adb devices on command line
----------------------------------------------------------------------------------
Step 5 : Make device ready
 - enable developer mode
 - make USB Debugging on
----------------------------------------------------------------------------------
Step 6 : Connect device to computer system thorugh USB cable
 - if asked enable USB Debbugging
----------------------------------------------------------------------------------
Step 7 : Run command adb devices
  adb = android debug bridge
 Check your device id displayed


1. Install Appium from:https://github.com/appium/appium-desktop/releases/tag/v1.15.1

commands:

adb devices
--> This will show the list of all the mobile devices connected to the windows.

2. To see the current app info(make sure app is open in phone):
adb shell
$ dumpsys window windows | grep -E 'mCurrentFocus'

--> this will give the apkpackage name.

3. Open App info app to see the appActivity

4. Desire capabilities:

AmazonApp desire capabilities:
{
  "automationName": "Appium",
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "ce11160bab38a11e04",
  "appPackage": "in.amazon.mShop.android.shopping",
  "appActivity": "com.amazon.mShop.home.HomeActivity"
}
----------------------------------------------------------------------------------
Links:
1. Appium Desired Capabilities:http://appium.io/docs/en/writing-running-appium/caps/
2. KeyEvent: https://developer.android.com/reference/android/view/KeyEvent
----------------------------------------------------------------------------------
