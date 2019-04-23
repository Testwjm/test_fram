import time
from pageobjects.fund_manager import FundManager
from testsuites.MyTest import MyTest


class TestFundManager(MyTest):
    """基金经理详情页"""

    def test_fund_manager_case1(self):
        fund = FundManager(self.driver)
        fund.fund_manager_login()
