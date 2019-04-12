import time
from pageobjects.public_manager import PowerPublicManager
from testsuites.MyTest import MyTest


class FofPowerPublicManager(MyTest):
    """公募基金经理详情页"""

    def test_public_manager_pass(self):
        public = PowerPublicManager
        public.public_manager_pass()
