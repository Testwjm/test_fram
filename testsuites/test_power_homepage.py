import time
from pageobjects.power_homepage import PowerHomePage
from testsuites.MyTest import MyTest


class FofPowerHomePage(MyTest):
    def test_power_a(self):
        homepage = PowerHomePage(self.driver)
        homepage.power_homepage_public()
        