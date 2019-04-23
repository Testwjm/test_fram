import time
from pageobjects.public_currency_fund import PublicCurrencyFund
from testsuites.MyTest import MyTest


class TestPublicCurrencyFund(MyTest):
    """公募货币型基金详情页"""

    def test_public_currency_fund_case1(self):
        """登录"""
        public = PublicCurrencyFund(self.driver)
        public.public_fund_login()

    def test_public_currency_fund_case2(self):
        pass
