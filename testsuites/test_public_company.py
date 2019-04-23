import time
from pageobjects.public_company import PublicCompany
from testsuites.MyTest import MyTest


class TestPublicCompany(MyTest):
    """公募公司详情页"""

    def public_company_case1(self):
        """登录"""
        public = PublicCompany(self.driver)
        public.public_company_login()

    def public_company_case2(self):
        public = PublicCompany(self.driver)
        pass