import os
import inspect


class TestData:
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    HTML_Report_Path = parent_dir + "\Reports"
    desired_cap = {
        "platformName": 'Android',
        "platformVersion": '8.0.0',
        "deviceName": "ce11160bab38a11e04",
        "appPackage": "in.amazon.mShop.android.shopping",
        "appActivity": 'com.amazon.mShop.home.HomeActivity'}
    host = 'http://127.0.0.1:4723/wd/hub'
    search_item_text = 'Apple iPhone 11 Pro Max, 64GB, Midnight Green'
    pin_code = '560037'