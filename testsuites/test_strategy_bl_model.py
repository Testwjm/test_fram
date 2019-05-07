import time
from pageobjects.strategy_bl_model import StrategyBlModel
from testsuites.my_test import MyTest


class TestStrategyBlModel(MyTest):
    """策略组合-BL模型"""

    def test_strategy_bl_case1(self):
        """登录"""
        strategy = StrategyBlModel(self.driver)
        strategy.strategy_bl_login()

    def test_strategy_bl_case2(self):
        """创建新的策略组合"""
        strategy = StrategyBlModel(self.driver)
        strategy.strategy_bl_establish()
