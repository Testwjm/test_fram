import time
from testsuites.MyTest import MyTest
from pageobjects.my import PowerMy
from framework.login import Login


class FofPowerMy(MyTest):
    """我的"""

    def test_a(self):
        Login().login(self.driver)

    def test_my_a(self):
        my = PowerMy(self.driver)
        my.power_my_login()
        my.power_my_click()
        time.sleep(2)
