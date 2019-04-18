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
        # 断言，会员类型
        error_mes = private.find_element(
            'xpath=>//*[@id="memberType"]').text
        try:
            assert error_mes == u'普通会员'
            print('会员类型 pass')
        except Exception as e:
            print('会员类型 fail', format(e))
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

    def test_private_company_etrend(self):
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
            'xpath=>//*[@id="righttitle"]/span').text
        try:
            assert error_mes == u'投顾综合指数走势'
            print('投顾综合指数走势 pass')
        except Exception as e:
            print('投顾综合指数走势 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.private_company_trend()

    def test_private_company_frank(self):
        """同类排名"""
        private = PrivateCompany(self.driver)
        private.private_company_rank()
        error_mes1 = private.find_element(
            'xpath=>//*[@id="rankingText"]').text
        error_mes = error_mes1.split('，')[0]  # # 获取这句话逗号前的语句
        try:
            assert error_mes == u'中期综合评价中'
            print('中期综合评价 pass')
        except Exception as e:
            print('中期综合评价 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = private.find_element('xpath=>//*[@id="rankingText"]/i[1]').text  # 获取近一年语句的排名
        one = one.replace('(', '').replace(')', '')  # 处理获取的值，去掉括号
        time.sleep(2)
        tow = private.find_element('xpath=>//*[@id="y1"]').text  # 获取近一年图表的排名
        try:  # 对比两者是否相同
            assert one == tow
            print('近一年排名一致 pass')
        except Exception as e:
            print('近一年排名不一致 fail', format(e))
        time.sleep(2)
        # 断言，投资顾问简介
        error_mes = private.find_element('xpath=>//*[@id="proFile"]').text
        try:
            assert error_mes == u'上海高毅资产管理合伙企业（有限合伙）是国内投研实力较强、管理规模较大、激励制度领先的平台型' \
                                u'私募基金管理公司，专注于资本市场，致力于为优秀的投资经理配备一流的研究支持、渠道资源、品牌' \
                                u'背书、资本对接和运营维护，打造以人为本的企业文化和扁平化的组织架构，让优秀的投资经理专注' \
                                u'于投资，全力以赴地为投资者创造更佳的收益。'
            print('私募投顾投资顾问简介 pass')
        except Exception as e:
            print('私募投顾投资顾问简介 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.execute_script()
        time.sleep(2)

    def test_private_company_grecord(self):
        """备案信息"""
        private = PrivateCompany(self.driver)
        private.private_record_information()
        # 断言，机构诚信信息
        error_mes = private.find_element('xpath=>//*[@id="creditInfo"]/tr/td[2]').text
        try:
            assert error_mes == u'无诚信信息'
            print('机构诚信信息 pass')
        except Exception as e:
            print('机构诚信信息 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 会员信息
        # 断言，会员信息
        error_mes = private.find_element(
            'xpath=>//*[@id="main-content"]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/span').text
        try:
            assert error_mes == u'普通会员'
            print('会员信息 pass')
        except Exception as e:
            print('会员信息 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 机构信息
        # 断言，私募投顾机构信息
        error_mes = private.find_element(
            'xpath=>//*[@id="managerInfo"]/div/div[3]/div/table/tbody/tr[1]/td[2]/span').text
        try:
            assert error_mes == u'上海高毅资产管理合伙企业（有限合伙）'
            print('机构信息 pass')
        except Exception as e:
            print('机构信息 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，登记编号
        error_mes = private.find_element(
            'xpath=>//*[@id="managerInfo"]/div/div[4]/div/table/tbody/tr[1]/td[2]/span').text
        try:
            assert error_mes == u'P1002305'
            print('登记编号 pass')
        except Exception as e:
            print('登记编号 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_company_hindicators(self):
        """业绩指标"""
        private = PrivateCompany(self.driver)
        private.private_performance_indicators()
        '''运营能力'''
        # 断言，今年以来累计收益率
        error_mes = private.find_element('xpath=>//*[@id="yearsYield"]').text
        try:
            assert error_mes != u'--'
            print('今年以来累计收益率 pass')
        except Exception as e:
            print('今年以来累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾员工数量
        error_mes = private.find_element('xpath=>//*[@id="numberOfemployees"]').text
        try:
            assert error_mes == u'78'
            print('员工数量 pass')
        except Exception as e:
            print('员工数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''盈利能力'''
        # 断言，统计区间
        error_mes = private.find_element('xpath=>//*[@id="profitabilityTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募全市场指数盈利能力
        error_mes = private.find_element('xpath=>//*[@id="profitabilityTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('私募全市场指数盈利能力 pass')
        except Exception as e:
            print('私募全市场指数盈利能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，沪深300指数盈利能力
        error_mes = private.find_element('xpath=>//*[@id="profitabilityTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('沪深300指数盈利能力 pass')
        except Exception as e:
            print('沪深300指数盈利能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，本公司盈利能力
        error_mes = private.find_element('xpath=>//*[@id="profitabilityTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('本公司盈利能力 pass')
        except Exception as e:
            print('本公司盈利能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''风控能力'''
        # 断言，统计区间
        error_mes = private.find_element('xpath=>//*[@id="windcontrolTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募全市场指数风控能力
        error_mes = private.find_element('xpath=>//*[@id="windcontrolTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('私募全市场指数风控能力 pass')
        except Exception as e:
            print('私募全市场指数风控能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，沪深300指数风控能力
        error_mes = private.find_element('xpath=>//*[@id="windcontrolTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('沪深300指数风控能力 pass')
        except Exception as e:
            print('沪深300指数风控能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，本公司风控能力
        error_mes = private.find_element('xpath=>//*[@id="windcontrolTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('本公司风控能力 pass')
        except Exception as e:
            print('本公司风控能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''投研能力'''
        # 断言，私募投顾统计区间
        error_mes = private.find_element('xpath=>//*[@id="investmentTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾择时能力
        error_mes = private.find_element('xpath=>//*[@id="investmentTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('择时能力 pass')
        except Exception as e:
            print('择时能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾选股能力
        error_mes = private.find_element('xpath=>//*[@id="investmentTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('选股能力 pass')
        except Exception as e:
            print('选股能力 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，私募投顾超额收益可持续性
        error_mes = private.find_element('xpath=>//*[@id="investmentTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('超额收益可持续性 pass')
        except Exception as e:
            print('超额收益可持续性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = private.find_element('xpath=>//*[@id="investmentTbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.execute_script()
        time.sleep(2)

    def test_private_company_iproducts(self):
        """旗下产品"""
        private = PrivateCompany(self.driver)
        private.private_its_products()
        # 断言，投资策略筛选
        error_mes = private.find_element('xpath=>//*[@id="main-grid"]/tbody/tr/td').text
        try:
            assert error_mes == u'没有找到匹配的记录'
            print('投资策略筛选 pass')
        except Exception as e:
            print('投资策略筛选 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益风险比
        error_mes = private.find_element('xpath=>//*[@id="main-content"]/div/div/div[2]/div[3]/div[2]/span').text
        try:
            assert error_mes == u'收益风险比'
            print('收益风险比 pass')
        except Exception as e:
            print('收益风险比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品相关性矩阵
        error_mes = private.find_element('xpath=>//*[@id="main-content"]/div/div/div[2]/div[5]/div[2]/span').text
        try:
            assert error_mes == u'产品相关性矩阵'
            print('产品相关性矩阵 pass')
        except Exception as e:
            print('产品相关性矩阵 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.execute_script()
        time.sleep(2)

    def test_private_company_jteam(self):
        """团队信息"""
        private = PrivateCompany(self.driver)
        private.private_team_information()
        private.current_handel()
        time.sleep(2)
        # 断言，基金经理链接
        try:
            assert u"私募基金经理详情页" in private.get_page_title()
            print('基金经理链接 pass')
        except Exception as e:
            print('基金经理链接 fail', format(e))
        time.sleep(2)
        private.close()
        private.current_handel()
        time.sleep(2)
        # 断言，产品相关性矩阵
        error_mes = private.find_element('xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('私募投资年限（年） pass.')
        except Exception as e:
            print('私募投资年限（年） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，管理数量
        error_mes = private.find_element('xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('管理数量 pass')
        except Exception as e:
            print('管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，履历背景
        error_mes = private.find_element('xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('履历背景 pass')
        except Exception as e:
            print('履历背景 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，擅长策略
        error_mes = private.find_element('xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('擅长策略 pass')
        except Exception as e:
            print('擅长策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[7]/a').click()
        private.current_handel()
        time.sleep(2)
        # 断言，代表产品链接
        try:
            assert u"高毅利伟精选唯实1号" in private.get_page_title()
            print('代表产品链接 pass')
        except Exception as e:
            print('代表产品链接 fail', format(e))
        time.sleep(2)
