import time
from pageobjects.industry_data import IndustryData
from testsuites.MyTest import MyTest


class TestIndustryData(MyTest):
    """行业数据"""

    def test_industry_data_alogin(self):
        industry = IndustryData(self.driver)
        industry.industry_data_login()
