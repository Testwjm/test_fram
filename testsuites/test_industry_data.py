import time
from pageobjects.industry_data import PowerIndustryData
from testsuites.MyTest import MyTest


class FofPowerIndustryData(MyTest):
    """行业数据"""

    def test_industry_data_pass(self):
        industry = PowerIndustryData
        industry.industry_data_pass()
