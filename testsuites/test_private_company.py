import time
from pageobjects.private_company import PrivateCompany
from testsuites.MyTest import MyTest


class TestPrivateCompany(MyTest):
    """私募公司详情页"""

    def test_private_company_alogin(self):
        """登录"""
        private = PrivateCompany(self.driver)
        private.private_company_login()

    def test_private_company_bdetails(self):
        """进入详情页"""
        private = PrivateCompany(self.driver)
        private.private_company_details()
        private.current_handel()
        # 断言，详情页
        try:
            assert u"上海高毅资产" in private.get_page_title()
            print('上海高毅资产详情 pass')
        except Exception as e:
            print('上海高毅资产详情 fail', format(e))
        time.sleep(2)

    def test_private_company_curl(self):
        """头部，公司网址"""
        private = PrivateCompany(self.driver)
        # 断言，投资策略
        error_mes = private.find_element(
            'xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes == u'股票多头'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公司代码
        error_mes = private.find_element(
            'xpath=>//*[@id="recordNumber"]').text
        try:
            assert error_mes == u'P1002305'
            print('公司代码 pass')
        except Exception as e:
            print('公司代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，自主发行规模
        error_mes = private.find_element(
            'xpath=>//*[@id="assetScale"]').text
        try:
            assert error_mes == u'50亿以上'
            print('自主发行规模 pass')
        except Exception as e:
            print('自主发行规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，顾问管理规模
        error_mes = private.find_element(
            'xpath=>//*[@id="consultantsScale"]').text
        try:
            assert error_mes == u'50亿以上'
            print('顾问管理规模 pass')
        except Exception as e:
            print('顾问管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，管理产品数量
        error_mes = private.find_element(
            'xpath=>//*[@id="productQuantity"]').text
        try:
            assert error_mes != u'--'
            print('管理产品数量 pass')
        except Exception as e:
            print('管理产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾会员类型
        error_mes = private.find_element(
            'xpath=>//*[@id="memberType"]').text
        try:
            assert error_mes == u'普通会员'
            print('私募投顾会员类型 pass')
        except Exception as e:
            print('私募投顾会员类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，所在地区
        error_mes = private.find_element(
            'xpath=>//*[@id="Area"]').text
        try:
            assert error_mes == u'广东'
            print('所在地区 pass')
        except Exception as e:
            print('所在地区 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾成立日期
        error_mes = private.find_element(
            'xpath=>//*[@id="dateEstablishment"]').text
        try:
            assert error_mes == u'2013-05-29'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.private_company_url()
        private.current_handel()
        time.sleep(2)
        # 断言，公司网址
        try:
            assert u"上海高毅资产" not in private.get_page_title()
            print('公司网址 pass')
        except Exception as e:
            print('公司网址 fail', format(e))
        time.sleep(2)
        private.back()
        time.sleep(5)
        private.current_handel()
        time.sleep(2)

    def test_private_company_dpersonnel(self):
        """核心人员"""
        private = PrivateCompany(self.driver)
        private.private_company_personnel()
        private.current_handel()
        time.sleep(2)
        # 断言，核心人员
        try:
            assert u"私募基金经理详情页" in private.get_page_title()
            print('核心人员 pass')
        except Exception as e:
            print('核心人员 fail', format(e))
        time.sleep(2)
        private.close()
        private.current_handel()
        time.sleep(2)

    def test_private_company_trend(self):
        """投顾综合指数走势"""
        private = PrivateCompany(self.driver)
        # 断言，产品分布
        error_mes = private.find_element(
            'xpath=>//*[@id="main-content"]/div/div/div[1]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'产品分布'
            print('产品分布 pass')
        except Exception as e:
            print('产品分布 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投顾综合指数走势
        error_mes = private.find_element(
            'xpath=>////*[@id="righttitle"]/span').text
        try:
            assert error_mes == u'投顾综合指数走势'
            print('投顾综合指数走势 pass')
        except Exception as e:
            print('投顾综合指数走势 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.private_company_trend()

    def test_private_company_rank(self):
        """同类排名"""
        private = PrivateCompany(self.driver)
        private.private_company_rank()
        error_mes = private.find_element(
            'xpath=>//*[@id="rankingText"]').text
        error_mes = error_mes.split(',')[0]  # # 获取这句话逗号前的语句
        try:
            assert error_mes == u'中期综合评价中'
            print('投顾综合指数走势 pass')
        except Exception as e:
            print('投顾综合指数走势 fail', format(e))
            print(error_mes)
        time.sleep(2)
        