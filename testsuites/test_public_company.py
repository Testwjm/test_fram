import time
from pageobjects.public_company import PublicCompany
from testsuites.MyTest import MyTest


class TestPublicCompany(MyTest):
    """公募公司详情页"""

    def public_company_alogin(self):
        public = PublicCompany(self.driver)
        public.public_company_login()
