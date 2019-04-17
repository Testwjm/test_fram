import time
from testsuites.MyTest import MyTest
from pageobjects.my import My


class TestMy(MyTest):
    """我的"""

    def test_my_alogin(self):
        my = My(self.driver)
        my.my_login()
