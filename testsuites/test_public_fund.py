import time
from pageobjects.public_fund import PowerPublicFund
from testsuites.MyTest import MyTest


class FofPowerPublicFund(MyTest):
    """公募基金详情页"""

    def test_public_fund_pass(self):
        public = PowerPublicFund(self.driver)
        public.public_fund_pass()
