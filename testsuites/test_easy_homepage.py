import time
from pageobjects.power_homepage import FofPowerHomepage
from testsuites.MyTest import MyTest


class PowerHomepage(MyTest):

    def test_power_search(self):
        homepage = FofPowerHomepage(self.driver)
        homepage
