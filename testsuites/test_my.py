import time
from testsuites.MyTest import MyTest
from pageobjects.my import My


class TestMy(MyTest):
    """我的"""

    def test_my_case1(self):
        my = My(self.driver)
        my.my_login()
