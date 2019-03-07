from framework.login import Login
import time
from pageobjects.power_my import FofPowerMy
from testsuites.MyTest import MyTest


class PowerMy(MyTest):

    def test_power_search(self):
        Login().login()
        homepage = FofPowerMy()
        homepage
