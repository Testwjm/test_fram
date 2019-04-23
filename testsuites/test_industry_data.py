import time
from pageobjects.industry_data import IndustryData
from testsuites.MyTest import MyTest


class TestIndustryData(MyTest):
    """行业数据"""

    def test_industry_data_case1(self):
        """登录"""
        industry = IndustryData(self.driver)
        industry.industry_data_login()

    def test_industry_data_case2(self):
        """私募登记备案情况"""
        industry = IndustryData(self.driver)
        # 断言，月份
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('月份 pass')
        except Exception as e:
            print('月份 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募证券管理人数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('私募证券管理人数量 pass')
        except Exception as e:
            print('私募证券管理人数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募股权创业管理人数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('私募股权创业管理人数量 pass.')
        except Exception as e:
            print('私募股权创业管理人数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募其他管理人数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('私募其他管理人数量 pass')
        except Exception as e:
            print('私募其他管理人数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        industry.industry_data_situation()
        # 断言，月份
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('月份 pass')
        except Exception as e:
            print('月份 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募证券基金产品数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('私募证券基金产品数量 pass')
        except Exception as e:
            print('私募证券基金产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募股权创业基金产品数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('私募股权创业基金产品数量 pass')
        except Exception as e:
            print('私募股权创业基金产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募其他基金产品数量
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('私募其他基金产品数量 pass')
        except Exception as e:
            print('私募其他基金产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        industry.find_element('xpath=>//*[@id="assetUl"]/li[3]').click()
        time.sleep(5)
        # 断言，月份
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('月份 pass')
        except Exception as e:
            print('月份 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募股权创业基金规模(亿元)
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('私募股权创业基金规模(亿元) pass')
        except Exception as e:
            print('私募股权创业基金规模(亿元) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募其他基金规模(亿元)
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('私募其他基金规模(亿元) pass')
        except Exception as e:
            print('私募其他基金规模(亿元) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募证券基金规模(亿元)
        error_mes = industry.find_element('xpath=>//*[@id="managerTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('私募证券基金规模(亿元) pass')
        except Exception as e:
            print('私募证券基金规模(亿元) fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_industry_data_case3(self):
        """指数涨跌风向标"""
        industry = IndustryData(self.driver)
        industry.industry_data_drogue()
        # 断言，指数涨跌风向标
        error_mes = industry.find_element('xpath=>//*[@id="comConfig"]/div/div[1]/div/div[5]/div[2]/span').text
        try:
            assert error_mes == u'指数涨跌风向标'
            print('指数涨跌风向标 pass')
        except Exception as e:
            print('指数涨跌风向标 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_industry_data_case4(self):
        """策略指数走势"""
        industry = IndustryData(self.driver)
        industry.industry_data_trend()

    def test_industry_data_case5(self):
        """指数相关性"""
        industry = IndustryData(self.driver)
        industry.industry_data_relativity()
        industry.execute_script()
        time.sleep(2)

    def test_industry_data_case6(self):
        """指数列表"""
        industry = IndustryData(self.driver)
        industry.industry_data_list()

