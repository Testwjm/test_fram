import time
from pageobjects.public_manager import PublicManager
from testsuites.MyTest import MyTest


class TestPublicManager(MyTest):
    """公募基金经理详情页"""

    def test_public_manager_alogin(self):
        public = PublicManager(self.driver)
        public.public_manager_login()
