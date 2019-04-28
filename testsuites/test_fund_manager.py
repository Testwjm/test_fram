import time
from pageobjects.fund_manager import FundManager
from testsuites.my_test import MyTest


class TestFundManager(MyTest):
    """基金经理筛选"""

    def test_fund_manager_case1(self):
        fund = FundManager(self.driver)
        fund.fund_manager_login()
