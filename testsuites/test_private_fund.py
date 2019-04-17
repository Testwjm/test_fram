import time
from pageobjects.private_fund import PrivateFund
from testsuites.MyTest import MyTest


class TestPrivateFund(MyTest):
    """私募基金详情页"""

    def test_private_fund_alogin(self):
        private = PrivateFund(self.driver)
        private.private_fund_login()


