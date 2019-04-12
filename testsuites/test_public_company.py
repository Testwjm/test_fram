import time
from pageobjects.public_company import PowerPublicCompany
from testsuites.MyTest import MyTest


class FofPowerPublicCompany(MyTest):
    """公募公司详情页"""

    def public_company_pass(self):
        public = PowerPublicCompany(self.driver)
        public.public_company_pass()
