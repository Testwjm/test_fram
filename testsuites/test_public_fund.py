import time
from pageobjects.public_fund import PublicFund
from testsuites.MyTest import MyTest


class TestPublicFund(MyTest):
    """公募基金详情页"""

    def test_public_fund_alogin(self):
        public = PublicFund(self.driver)
        public.public_fund_login()

