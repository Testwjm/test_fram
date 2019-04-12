import time
from pageobjects.private_company import PowerPrivateCompany
from testsuites.MyTest import MyTest


class FofPowerPrivateCompany(MyTest):
    """私募公司详情页"""

    def private_company_pass(self):
        private = PowerPrivateCompany(self.driver)
        private.private_company_pass()
