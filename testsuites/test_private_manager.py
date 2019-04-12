import time
from pageobjects.private_manager import PowerPrivateManager
from testsuites.MyTest import MyTest


class FofPowerPrivateManager(MyTest):
    """私募基金经理详情页"""

    def test_private_manager_pass(self):
        private = PowerPrivateManager(self.driver)
        private.private_manager_pass()
