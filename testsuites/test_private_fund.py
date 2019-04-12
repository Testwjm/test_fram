import time
from pageobjects.private_fund import PowerPrivateFund
from testsuites.MyTest import MyTest


class FofPowerPrivateFund(MyTest):
    """私募基金详情页"""

    def test_private_fund_pass(self):
        private = PowerPrivateFund(self.driver)
        private.private_fund_pass()

