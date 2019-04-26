import time
from pageobjects.public_currency_fund import PublicCurrencyFund
from testsuites.MyTest import MyTest


class TestPublicCurrencyFund(MyTest):
    """公募货币型基金详情页"""

    def test_public_currency_fund_case1(self):
        """登录"""
        public = PublicCurrencyFund(self.driver)
        public.public_currency_fund_login()

    def test_public_currency_fund_case2(self):
        """头部"""
        public = PublicCurrencyFund(self.driver)
        public.public_currency_fund_details()
        public.current_handel()
        time.sleep(2)
        # 断言，公募货币型基金详情页
        try:
            assert u"易方达天天理财货币A" in public.get_page_title()
            print('公募货币型基金详情 pass')
        except Exception as e:
            print('公募货币型基金详情 fail', format(e))
        time.sleep(2)
        '''头部'''
        # 断言，头部显示策略
        error_mes = public.find_element(
            'xpath=>//*[@id="Policy"]').text  # 货币型基金
        try:
            assert error_mes == u'货币型基金-货币型'
            print('头部显示货币型基金 pass')
        except Exception as e:
            print('头部显示货币型基金 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示代码
        error_mes = public.find_element(
            'xpath=>//*[@id="reg_code"]').text
        try:
            assert error_mes == u'(000600)'
            print('头部显示代码 pass')
        except Exception as e:
            print('头部显示代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示标签
        error_mes = public.find_element(
            'xpath=>//*[@id="prcInfo"]/div[1]/div[1]/div[2]/div[2]/span[2]').text
        try:
            assert error_mes == u'低风险(R1)'
            print('头部显示标签 pass')
        except Exception as e:
            print('头部显示标签 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示净值日期
        error_mes = public.find_element(
            'xpath=>//*[@id="nav_date2"]').text
        try:
            assert error_mes != u'--'
            print('头部显示净值日期 pass')
        except Exception as e:
            print('头部显示净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示七日年化收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="d7_return_a"]').text  # 3.70%
        try:
            assert error_mes != u'--'
            print('头部显示七日年化收益率 pass')
        except Exception as e:
            print('头部显示七日年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示万份收益
        error_mes = public.find_element(
            'xpath=>//*[@id="return_10k"]').text
        try:
            assert error_mes != u'--'
            print('头部显示万份收益 pass')
        except Exception as e:
            print('头部显示万份收益 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示七日年化排名
        error_mes = public.find_element(
            'xpath=>//*[@id="coin"]/div[1]/div/div[4]/div[1]').text
        try:
            assert error_mes != u'/'
            print('头部显示七日年化排名 pass')
        except Exception as e:
            print('头部显示七日年化排名 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示成立日期
        error_mes = public.find_element(
            'xpath=>//*[@id="foundation_date2"]').text  # 2014-05-28
        try:
            assert error_mes == u'2014-05-28'
            print('头部显示成立日期 pass')
        except Exception as e:
            print('头部显示成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示基金公司名称
        error_mes = public.find_element(
            'xpath=>//*[@id="org_name2"]').text
        try:
            assert error_mes == u'汇添富'
            print('头部显示基金公司名称 pass')
        except Exception as e:
            print('头部显示基金公司名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头部显示基金经理
        error_mes = public.find_element(
            'xpath=>//*[@id="coin"]/div[2]/div/div/div[2]/span[2]').text
        try:
            assert error_mes == u'徐寅喆'
            print('头部显示基金经理 pass')
        except Exception as e:
            print('头部显示基金经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="org_name2"]').click()  # 基金公司链接
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        # 断言，基金公司链接
        try:
            assert u"易方达基金管理有限公司" in public.get_page_title()
            print('基金公司链接 pass')
        except Exception as e:
            print('基金公司链接 fail', format(e))
        time.sleep(2)
        public.back()
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        public.find_element('xpath=>//*[@id="coin"]/div[2]/div/div/div[2]/span[2]/a[1]').click()  # 基金经理链接
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        # 断言，基金经理链接
        try:
            assert u"公募基金经理详情页" in public.get_page_title()
            print('基金经理链接 pass')
        except Exception as e:
            print('基金经理链接 fail', format(e))
        time.sleep(2)
        public.close()
        time.sleep(2)
        public.current_handel()
        time.sleep(2)

    def test_public_currency_fund_case3(self):
        """历史净值"""
        public = PublicCurrencyFund(self.driver)
        public.public_currency_fund_history()
        # 断言，净值日期
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，万份收益
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[2]').text  # 万份收益
        try:
            assert error_mes != u'--'
            print('万份收益 pass')
        except Exception as e:
            print('万份收益 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，7日年化
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('7日年化 pass')
        except Exception as e:
            print('7日年化 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_currency_fund_case4(self):
        """基本信息"""
        public = PublicCurrencyFund(self.driver)
        public.public_currency_fund_info()
        # 断言，基本信息
        error_mes = public.find_element(
            'xpath=>//*[@id="fundName"]').text  # 汇添富和聚宝货币
        try:
            assert error_mes == u'汇添富和聚宝货币'
            print('基本信息 pass')
        except Exception as e:
            print('基本信息 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，投资经理简介
        error_mes1 = public.find_element(
            'xpath=>//*[@id="infoDetail"]/div[2]').text
        error_mes = error_mes1.split('：')[0]  # # 获取这句话逗号前的语句
        try:
            assert error_mes == u'徐寅喆女士'
            print('投资经理简介 pass')
        except Exception as e:
            print('投资经理简介 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，投资顾问简介
        error_mes = public.find_element(
            'xpath=>//*[@id="proFile"]/div').text
        try:
            assert error_mes == u'暂无信息'
            print('投资顾问简介 pass')
        except Exception as e:
            print('投资顾问简介 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_currency_fund_case5(self):
        """持仓分析"""
        public = PublicCurrencyFund(self.driver)
        public.public_currency_fund_position()
        # 断言，资产配置标题
        error_mes = public.find_element(
            'xpath=>//*[@id="assetAllocation"]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'资产配置'
            print('资产配置标题 pass')
        except Exception as e:
            print('资产配置标题 fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，资产配置
        error_mes = public.find_element(
            'xpath=>//*[@id="flucture"]').text
        try:
            assert error_mes == u'减少'
            print('资产配置 pass')
        except Exception as e:
            print('资产配置 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 数据日期
        public.find_element('xpath=>//*[@id="assetdate"]').click()  # 点击数据日期框
        time.sleep(3)
        public.find_element('xpath=>//*[@id="assetdate"]/option[12]').click()  # 点击最后那个
        time.sleep(3)
        # 断言，数据日期
        error_mes = public.find_element(
            'xpath=>//*[@id="assetdate"]/option[12]').text
        try:
            assert error_mes != u'2018-09-30'
            print('数据日期 pass')
        except Exception as e:
            print('数据日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，资产账户
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('资产账户 pass')
        except Exception as e:
            print('资产账户 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，资产净值（亿元）
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('现金资产净值 pass')
        except Exception as e:
            print('现金资产净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，占资产比例
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('现金占资产比例 pass')
        except Exception as e:
            print('现金占资产比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，占比区间变化
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('现金占比区间变化 pass')
        except Exception as e:
            print('现金占比区间变化 fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，规模变动详情
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChange"]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'规模变动详情'
            print('规模变动详情 pass')
        except Exception as e:
            print('规模变动详情 fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，日期
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[2]/td[1]').text
        try:
            assert error_mes != u'--'
            print('日期 pass')
        except Exception as e:
            print('日期 fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，期间申购（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('期间申购（亿份） pass')
        except Exception as e:
            print('期间申购（亿份） fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，期间赎回（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[2]/td[3]').text
        try:
            assert error_mes != u'--'
            print('期间赎回（亿份） pass')
        except Exception as e:
            print('期间赎回（亿份） fail', format(e))
            print(error_mes)
        time.sleep(5)
        # 断言，净申购（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[2]/td[4]').text
        try:
            assert error_mes != u'--'
            print('净申购（亿份） pass')
        except Exception as e:
            print('净申购（亿份） fail', format(e))
            print(error_mes)
        time.sleep(5)
