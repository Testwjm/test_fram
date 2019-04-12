import time
from pageobjects.fund_manager import PowerFundManager
from testsuites.MyTest import MyTest


class FofPowerFundManager(MyTest):
    """基金经理详情页"""

    def test_fund_manager_pass(self):
        fund = PowerFundManager
        fund.fund_manager_pass()
