import time
from pageobjects.private_manager import PrivateManager
from testsuites.MyTest import MyTest


class TestPrivateManager(MyTest):
    """私募基金经理详情页"""

    def test_private_manager_case1(self):
        """登录"""
        private = PrivateManager(self.driver)
        private.private_manager_login()

    def test_private_manager_case2(self):
        """"""
