import time
from pageobjects.public_fund import PublicFund
from testsuites.my_test import MyTest


class TestPublicFund(MyTest):
    """公募基金详情页"""

    def test_public_fund_case1(self):
        """登录"""
        public = PublicFund(self.driver)
        public.public_fund_login()

    def test_public_fund_case2(self):
        """头部"""
        public = PublicFund(self.driver)
        public.public_fund_details()
        public.current_handel()
        # 断言，公募基金详情页
        try:
            assert u"华夏成长混合" in public.get_page_title()
            print('公募基金详情 pass')
        except Exception as e:
            print('公募基金详情 fail', format(e))
        time.sleep(2)
        # 断言，策略
        error_mes = public.find_element(
            'xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes != u'--'
            print('策略 pass')
        except Exception as e:
            print('策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，代码
        error_mes = public.find_element(
            'xpath=>//*[@id="reg_code"]').text
        try:
            assert error_mes != u'--'
            print('代码 pass')
        except Exception as e:
            print('代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，中高风险(R4)
        error_mes = public.find_element(
            'xpath=>//*[@id="prcInfo"]/div[1]/div[1]/div[2]/div[2]/span[2]').text
        try:
            assert error_mes == u'中高风险(R4)'
            print('中高风险(R4) pass')
        except Exception as e:
            print('中高风险(R4) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，星级
        error_mes = public.find_element(
            'xpath=>//*[@id="star"]').text
        try:
            assert error_mes == u''
            print('星级 pass')
        except Exception as e:
            print('星级 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = public.find_element(
            'xpath=>//*[@id="nav_date"]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = public.find_element(
            'xpath=>//*[@id="netNav"]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = public.find_element(
            'xpath=>//*[@id="added_nav"]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = public.find_element(
            'xpath=>//*[@id="swanav"]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指标日期
        error_mes = public.find_element(
            'xpath=>//*[@id="sdate"]').text
        try:
            assert error_mes != u'--'
            print('指标日期 pass')
        except Exception as e:
            print('指标日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，近一月收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="m1_return"]').text
        try:
            assert error_mes != u'--'
            print('近一月收益率 pass')
        except Exception as e:
            print('近一月收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，今年以来收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="year_return"]').text
        try:
            assert error_mes != u'--'
            print('今年以来收益率 pass')
        except Exception as e:
            print('今年以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立以来收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="total_return"]').text
        try:
            assert error_mes != u'--'
            print('成立以来收益率 pass')
        except Exception as e:
            print('成立以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资顾问
        error_mes = public.find_element(
            'xpath=>//*[@id="org_name"]').text
        try:
            assert error_mes == u'华夏基金'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = public.find_element(
            'xpath=>//*[@id="foundation_date"]').text  # 2001-12-18
        try:
            assert error_mes == u'2001-12-18'
            print('头部显示成立日期 pass')
        except Exception as e:
            print('头部显示成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金经理
        error_mes = public.find_element(
            'xpath=>//*[@id="main"]/div[3]/div/div/div[2]/span[2]/span').text  # 董阳阳
        try:
            assert error_mes == u'董阳阳'
            print('头部显示基金经理 pass')
        except Exception as e:
            print('头部显示基金经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="org_name"]').click()
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        # 断言，投资顾问链接
        try:
            assert u"华夏基金管理有限公司" in public.get_page_title()
            print('投资顾问链接 pass')
        except Exception as e:
            print('投资顾问链接 fail', format(e))
        time.sleep(2)
        public.back()
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        public.find_element('xpath=>//*[@id="main"]/div[3]/div/div/div[2]/span[2]/span').click()
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

    def test_public_fund_case3(self):
        """历史净值"""
        public = PublicFund(self.driver)
        public.public_fund_history()
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
        # 断言，单位净值
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = public.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_fund_case4(self):
        """同类排名"""
        public = PublicFund(self.driver)
        public.public_fund_rank()
        error_mes1 = public.find_element(
            'xpath=>//*[@id="rankingText"]').text
        error_mes = error_mes1.split('，')[0]  # # 获取这句话逗号前的语句
        try:
            assert error_mes == u'中期综合评价中'
            print('中期综合评价 pass')
        except Exception as e:
            print('中期综合评价 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = public.find_element('xpath=>//*[@id="rankingText"]/i[1]').text  # 获取近一年语句的排名
        one = one.replace('(', '').replace(')', '')  # 处理获取的值，去掉括号
        time.sleep(2)
        tow = public.find_element('xpath=>//*[@id="y1"]').text  # 获取近一年图表的排名
        try:  # 对比两者是否相同
            assert one == tow
            print('近一年排名一致 pass')
        except Exception as e:
            print('近一年排名不一致 fail', format(e))
        time.sleep(2)

    def test_public_fund_case5(self):
        """指标"""
        public = PublicFund(self.driver)
        public.public_fund_index()
        '''收益指标'''
        # 断言，统计区间
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金累计收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金累计收益率 pass')
        except Exception as e:
            print('基金累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        # 断言，统计区间
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金年化收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金年化收益率 pass')
        except Exception as e:
            print('基金年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300年化收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300年化收益率 pass')
        except Exception as e:
            print('hs300年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''风险指标'''
        # 断言，VaR
        error_mes = public.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = public.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，波动率
        error_mes = public.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = public.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''动态回撤'''
        public.find_element('xpath=>//*[@id="showAll1"]').click()
        time.sleep(5)
        '''风险调整收益指标'''
        # 断言，统计区间
        error_mes = public.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金风险调整收益指标
        error_mes = public.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金风险调整收益指标 pass')
        except Exception as e:
            print('基金风险调整收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300风险调整收益指标
        error_mes = public.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300风险调整收益指标 pass')
        except Exception as e:
            print('hs300风险调整收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''相对指标'''
        # 断言，统计区间
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = public.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.execute_script_up()

    def test_public_fund_case6(self):
        """基本信息"""
        public = PublicFund(self.driver)
        public.public_fund_info()
        # 断言，基本信息
        error_mes = public.find_element(
            'xpath=>//*[@id="fund_full_name"]').text  # 基金全称
        try:
            assert error_mes == u'易方达天天理财货币A'
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
            assert error_mes == u'刘朝阳女士'
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
        public.execute_script_up()
        time.sleep(2)

    def test_public_fund_case7(self):
        """持仓分析"""
        public = PublicFund(self.driver)
        public.public_fund_positions()
        # 断言，资产配置名称
        error_mes = public.find_element(
            'xpath=>//*[@id="assetAllocation"]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'资产配置'
            print('资产配置名称 pass')
        except Exception as e:
            print('资产配置名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，资产配置
        error_mes = public.find_element(
            'xpath=>//*[@id="flucture"]').text
        try:
            assert error_mes == u'增加'
            print('资产配置 pass')
        except Exception as e:
            print('资产配置 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="assetdate"]/option[12]').click()  # 点击最后一个
        time.sleep(3)
        # 断言，数据日期
        error_mes = public.find_element(
            'xpath=>//*[@id="assetdate"]/option[12]').text
        try:
            assert error_mes != u'2018-09-30'
            print('资产配置数据日期 pass.')
        except Exception as e:
            print('资产配置数据日期 fail', format(e))
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
        time.sleep(3)
        # 断言，资产净值(亿元)
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('资产净值 pass')
        except Exception as e:
            print('资产净值 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，占资产比例
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('占资产比例 pass')
        except Exception as e:
            print('占资产比例 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，占比区间变化
        error_mes = public.find_element(
            'xpath=>//*[@id="assetTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('占比区间变化 pass')
        except Exception as e:
            print('占比区间变化 fail', format(e))
            print(error_mes)
        time.sleep(3)
        '''规模变动详情'''
        # 断言，规模变动详情
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChange"]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'规模变动详情'
            print('规模变动详情 pass')
        except Exception as e:
            print('规模变动详情 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，日期
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u''
            print('日期 pass')
        except Exception as e:
            print('日期 fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，期间申购（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('期间申购（亿份） pass')
        except Exception as e:
            print('期间申购（亿份） fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，期间赎回（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u''
            print('期间赎回（亿份） pass')
        except Exception as e:
            print('期间赎回（亿份） fail', format(e))
            print(error_mes)
        time.sleep(3)
        # 断言，净申购（亿份）
        error_mes = public.find_element(
            'xpath=>//*[@id="scaleChangeTable"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('净申购（亿份） pass')
        except Exception as e:
            print('净申购（亿份） fail', format(e))
            print(error_mes)
        time.sleep(3)
        '''股票行业分布'''
        # 断言，股票行业分布
        public.find_element('xpath=>//*[@id="stockIndustdate"]/option[12]').click()  # 点击最后一个
        time.sleep(3)
        # 断言，数据日期
        error_mes = public.find_element(
            'xpath=>//*[@id="stockIndustdate"]/option[12]').text
        try:
            assert error_mes != u'2018-09-30'
            print('股票行业分布数据日期 pass')
        except Exception as e:
            print('股票行业分布数据日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 股票行业分布行业类别
        error_mes = public.find_element(
            'xpath=>//*[@id="stockIndustTable"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('股票行业分布行业类别 pass')
        except Exception as e:
            print('股票行业分布行业类别 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 股票行业分布资产净值（万元）
        error_mes = public.find_element(
            'xpath=>//*[@id="stockIndustTable"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('股票行业分布资产净值 pass')
        except Exception as e:
            print('股票行业分布资产净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 股票行业分布占资产比例
        error_mes = public.find_element(
            'xpath=>//*[@id="stockIndustTable"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('股票行业分布占资产比例 pass')
        except Exception as e:
            print('股票行业分布占资产比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 股票行业分布占比区间变化
        error_mes = public.find_element(
            'xpath=>//*[@id="stockIndustTable"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票行业分布占比区间变化 pass')
        except Exception as e:
            print('股票行业分布占比区间变化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，前五大行业占资产比例
        error_mes = public.find_element(
            'xpath=>//*[@id="conPercent"]').text
        try:
            assert error_mes != u'--'
            print('前五大行业占资产比例 pass')
        except Exception as e:
            print('前五大行业占资产比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 重仓债券
        public.find_element('xpath=>//*[@id="li-mix"]').click()  # 点击重仓债券
        time.sleep(3)
        public.find_element('xpath=>//*[@id="heavyBonddate"]/option[12]').click()  # 点击最后一个
        time.sleep(3)
        # 断言，数据日期
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBonddate"]/option[12]').text
        try:
            assert error_mes != u'2018-09-30'
            print('重仓债券数据日期 pass')
        except Exception as e:
            print('重仓债券数据日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.execute_script_down()  # 浏览器往下
        time.sleep(2)
        # 断言，重仓债券债券代码
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('重仓债券债券代码 pass')
        except Exception as e:
            print('重仓债券债券代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓债券债券名称
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('重仓债券债券名称 pass')
        except Exception as e:
            print('重仓债券债券名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓债券持仓比例
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('重仓债券持仓比例 pass')
        except Exception as e:
            print('重仓债券持仓比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓债券持仓数量
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'-'
            print('重仓债券持仓数量 pass')
        except Exception as e:
            print('重仓债券持仓数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓债券持仓市值（万元）
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('重仓债券持仓市值 pass')
        except Exception as e:
            print('重仓债券持仓市值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓债券持仓变动
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyBondTbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('重仓债券持仓变动 pass')
        except Exception as e:
            print('重仓债券持仓变动 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 重仓持股
        public.find_element('xpath=>//*[@id="li-mix-stock"]').click()  # 点击重仓持股
        time.sleep(5)
        public.find_element('xpath=>//*[@id="heavyStockHolddate"]/option[12]').click()  # 点击最后一个
        time.sleep(3)
        # 断言，数据日期
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHolddate"]/option[12]').text
        try:
            assert error_mes != u'2018-09-30'
            print('重仓持股数据日期 pass')
        except Exception as e:
            print('重仓持股数据日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股股票代码
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('重仓持股股票代码 pass')
        except Exception as e:
            print('重仓持股股票代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股股票名称
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('重仓持股股票名称 pass')
        except Exception as e:
            print('重仓持股股票名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股持仓比例
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('重仓持股持仓比例 pass')
        except Exception as e:
            print('重仓持股持仓比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股持仓数量
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('重仓持股持仓数量 pass')
        except Exception as e:
            print('重仓持股持仓数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股持仓市值（万元）
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('重仓持股持仓市值 pass')
        except Exception as e:
            print('重仓持股持仓市值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，重仓持股持仓变动
        error_mes = public.find_element(
            'xpath=>//*[@id="heavyStockHoldTbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('重仓持股持仓变动 pass')
        except Exception as e:
            print('重仓持股持仓变动 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 浏览器到最上面
        public.execute_script_up()  # 浏览器往上
        time.sleep(3)

    def test_public_fund_case8(self):
        """夏普模型"""
        public = PublicFund(self.driver)
        public.public_fund_sharp()
        # 断言，大类资产占比情况
        error_mes = public.find_element(
            'xpath=>//*[@id="tab2"]/div[2]/div[1]/div[1]').text  # 大类资产占比情况
        try:
            assert error_mes == u'大类资产占比情况：'
            print('大类资产占比情况： pass')
        except Exception as e:
            print('大类资产占比情况： fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产占比情况语句
        one = public.find_element('xpath=>//*[@id="comment1"]').text  # 大类资产占比情况语句
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'从仓位模拟结果来看'
            print('大类资产占比情况语句 pass')
        except Exception as e:
            print('大类资产占比情况语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况
        error_mes = public.find_element(
            'xpath=>//*[@id="tab2"]/div[3]/div[1]/div[1]').text  # 风格因子占比情况：
        try:
            assert error_mes == u'风格因子占比情况：'
            print('风格因子占比情况： pass')
        except Exception as e:
            print('风格因子占比情况： fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况语句
        one = public.find_element('xpath=>//*[@id="comment2"]').text  # 风格因子占比情况语句
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'在风格配置方面'
            print('风格因子占比情况语句 pass')
        except Exception as e:
            print('风格因子占比情况语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 大类资产拟合优度
        # 断言，大类资产拟合优度语句
        one = public.find_element('xpath=>//*[@id="halfComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('大类资产拟合优度语句 pass')
        except Exception as e:
            print('大类资产拟合优度语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('大类资产 pass')
        except Exception as e:
            print('大类资产 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('风格因子 pass')
        except Exception as e:
            print('风格因子 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，权重
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes == u'--'
            print('权重 pass')
        except Exception as e:
            print('权重 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，P值
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'--'
            print('P值 pass')
        except Exception as e:
            print('P值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，显著标记
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes == u'--'
            print('显著标记 pass')
        except Exception as e:
            print('显著标记 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益贡献率
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('收益贡献率 pass')
        except Exception as e:
            print('收益贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，波动贡献率
        error_mes = public.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('波动贡献率 pass')
        except Exception as e:
            print('波动贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''风格变化'''
        # 断言，
        error_mes = public.find_element(
            'xpath=>//*[@id="tab2"]/div[5]/div[1]/div/div[2]/span').text
        try:
            assert error_mes == u'风格变化'
            print('风格变化 pass')
        except Exception as e:
            print('风格变化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益分解时序图
        error_mes = public.find_element(
            'xpath=>//*[@id="tab2"]/div[6]/div[1]/div[1]/div/span').text
        try:
            assert error_mes == u'收益分解时序图'
            print('收益分解时序图 pass')
        except Exception as e:
            print('收益分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风险分解时序图
        error_mes = public.find_element(
            'xpath=>//*[@id="tab2"]/div[6]/div[2]/div[1]/div/span').text
        try:
            assert error_mes == u'风险分解时序图'
            print('风险分解时序图 pass')
        except Exception as e:
            print('风险分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 浏览器到最上面
        public.execute_script_up()  # 浏览器往上
        time.sleep(3)

    def test_public_fund_case9(self):
        """FF模型"""
        public = PublicFund(self.driver)
        public.public_fund_ff()
        # 断言，三因子收益贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab3"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('三因子收益贡献分解 pass')
        except Exception as e:
            print('三因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子收益贡献分解语句
        one = public.find_element('xpath=>//*[@id="incomeComent"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'从外部归因来看'
            print('三因子收益贡献分解语句 pass')
        except Exception as e:
            print('三因子收益贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 三因子风险贡献分解
        # 断言，三因子风险贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab3"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('三因子风险贡献分解 pass')
        except Exception as e:
            print('三因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子风险贡献分解语句
        one = public.find_element('xpath=>//*[@id="riskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('三因子风险贡献分解语句 pass')
        except Exception as e:
            print('三因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 三因子暴露及相关性分析
        # 断言，三因子暴露及相关性分析
        error_mes = public.find_element(
            'xpath=>//*[@id="tab3"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes != u'--'
            print('三因子暴露及相关性分析 pass')
        except Exception as e:
            print('三因子暴露及相关性分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子暴露及相关性分析语句1
        one = public.find_element('xpath=>//*[@id="yzComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('三因子暴露及相关性分析语句1 pass')
        except Exception as e:
            print('三因子暴露及相关性分析语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子暴露及相关性分析语句2
        one = public.find_element('xpath=>//*[@id="yzComment2"]').text
        one = one.split('间')[0]  # 获取这句话间前的语句
        error_mes = one
        try:
            assert error_mes == u'因子之'
            print('三因子暴露及相关性分析语句2 pass')
        except Exception as e:
            print('三因子暴露及相关性分析语句2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子系数
        error_mes = public.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('三因子因子系数 pass')
        except Exception as e:
            print('三因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子系数值
        error_mes = public.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('三因子因子系数值 pass')
        except Exception as e:
            print('三因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子p值
        error_mes = public.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('三因子p值 pass')
        except Exception as e:
            print('三因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子拟合优度
        error_mes = public.find_element(
            'xpath=>//*[@id="r_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('三因子拟合优度 pass')
        except Exception as e:
            print('三因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        public.execute_script_up()  # 浏览器往上
        time.sleep(3)
        '''Carhart四因子'''
        public.find_element('xpath=>//*[@id="tab1"]/div[1]/label[2]').click()  # 点击Carhart四因子
        time.sleep(10)
        # 收益贡献分解
        # 断言，四因子收益贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab4"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('四因子收益贡献分解 pass')
        except Exception as e:
            print('四因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子收益贡献分解语句
        one = public.find_element('xpath=>//*[@id="incomeComent2"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'从外部归因来看'
            print('四因子收益贡献分解语句 pass')
        except Exception as e:
            print('四因子收益贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 四因子风险贡献分解
        # 断言，四因子风险贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab4"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('四因子风险贡献分解 pass')
        except Exception as e:
            print('四因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风险贡献分解语句
        one = public.find_element('xpath=>//*[@id="fourriskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('四因子风险贡献分解语句 pass')
        except Exception as e:
            print('四因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 四因子暴露及相关性分析
        # 断言，四因子暴露及相关性分析
        error_mes = public.find_element(
            'xpath=>//*[@id="tab4"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes != u'--'
            print('四因子暴露及相关性分析 pass')
        except Exception as e:
            print('四因子暴露及相关性分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子暴露及相关性分析语句1
        one = public.find_element('xpath=>//*[@id="fouryzComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('四因子暴露及相关性分析语句1 pass')
        except Exception as e:
            print('四因子暴露及相关性分析语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子暴露及相关性分析语句2
        one = public.find_element('xpath=>//*[@id="fouryzComment2"]').text
        one = one.split('间')[0]  # 获取这句话间前的语句
        error_mes = one
        try:
            assert error_mes == u'因子之'
            print('四因子暴露及相关性分析语句2 pass')
        except Exception as e:
            print('四因子暴露及相关性分析语句2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子系数
        error_mes = public.find_element(
            'xpath=>//*[@id="fourfit"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('四因子因子系数 pass')
        except Exception as e:
            print('四因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子系数值
        error_mes = public.find_element(
            'xpath=>//*[@id="fourfit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('四因子因子系数值 pass')
        except Exception as e:
            print('四因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子p值
        error_mes = public.find_element(
            'xpath=>//*[@id="fourfit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('四因子p值 pass')
        except Exception as e:
            print('四因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子拟合优度
        error_mes = public.find_element(
            'xpath=>//*[@id="fourr_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('四因子拟合优度 pass')
        except Exception as e:
            print('四因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        public.execute_script_up()  # 浏览器往上
        time.sleep(3)
        '''FF五因子'''
        public.find_element('xpath=>//*[@id="tab1"]/div[1]/label[3]').click()  # 点击FF五因子
        time.sleep(10)
        # 五因子收益贡献分解
        # 断言，五因子收益贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab5"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('五因子收益贡献分解 pass')
        except Exception as e:
            print('五因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子收益贡献分解语句
        one = public.find_element('xpath=>//*[@id="incomeComent3"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'从外部归因来看'
            print('五因子收益贡献分解语句 pass')
        except Exception as e:
            print('五因子收益贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 五因子风险贡献分解
        # 断言，五因子风险贡献分解
        error_mes = public.find_element(
            'xpath=>//*[@id="tab5"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('五因子风险贡献分解 pass')
        except Exception as e:
            print('五因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子风险贡献分解语句
        one = public.find_element('xpath=>//*[@id="fiveriskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('五因子风险贡献分解语句 pass')
        except Exception as e:
            print('五因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 五因子因子暴露及相关性分析
        # 断言，五因子因子暴露及相关性分析
        error_mes = public.find_element(
            'xpath=>//*[@id="tab5"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes == u'因子暴露及相关性分析'
            print('五因子因子暴露及相关性分析 pass')
        except Exception as e:
            print('五因子因子暴露及相关性分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子暴露及相关性分析语句1
        one = public.find_element('xpath=>//*[@id="fiveyzComment2"]').text
        one = one.split('间')[0]  # 获取这句话间前的语句
        error_mes = one
        try:
            assert error_mes == u'因子之'
            print('五因子暴露及相关性分析语句1 pass')
        except Exception as e:
            print('五因子暴露及相关性分析语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子暴露及相关性分析语句2
        one = public.find_element('xpath=>//*[@id="fiveyzComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('五因子因子暴露及相关性分析语句2 pass')
        except Exception as e:
            print('五因子因子暴露及相关性分析语句2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子系数
        error_mes = public.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('五因子因子系数 pass')
        except Exception as e:
            print('五因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子系数值
        error_mes = public.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('五因子因子系数值 pass')
        except Exception as e:
            print('五因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子p值
        error_mes = public.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('五因子p值 pass')
        except Exception as e:
            print('五因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子拟合优度
        error_mes = public.find_element(
            'xpath=>//*[@id="fiver_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('五因子拟合优度 pass')
        except Exception as e:
            print('五因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        public.execute_script_up()  # 浏览器往上
        time.sleep(3)

    def test_public_fund_case91(self):
        """持仓归因"""
        public = PublicFund(self.driver)
        public.public_fund_barra()
        # 断言，因子
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'市值'
            print('因子 pass')
        except Exception as e:
            print('因子 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化方差
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('年化方差 pass')
        except Exception as e:
            print('年化方差 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，因子暴露
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('因子暴露 pass')
        except Exception as e:
            print('因子暴露 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，因子有效性
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('因子有效性 pass')
        except Exception as e:
            print('因子有效性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，择时有效性
        error_mes = public.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('择时有效性 pass')
        except Exception as e:
            print('择时有效性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="barra_bck"]/button[2]').click()  # 点击年化方差
        time.sleep(5)
        public.find_element('xpath=>//*[@id="barra_bck"]/button[3]').click()  # 点击因子暴露
        time.sleep(5)
        public.find_element('xpath=>//*[@id="barra_bck"]/button[4]').click()  # 点击有效性研判
        time.sleep(5)

    def test_public_fund_case92(self):
        """情景分析"""
        public = PublicFund(self.driver)
        public.public_fund_scene()
        # A股市场
        # 断言，A股市场基金涨跌幅
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('A股市场基金涨跌幅 pass')
        except Exception as e:
            print('A股市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，A股市场沪深300涨跌幅
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('A股市场沪深300涨跌幅 pass')
        except Exception as e:
            print('A股市场沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 债券固收市场
        public.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击债券固收市场
        time.sleep(3)
        # 断言，债券固收市场基金涨跌幅
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('债券固收市场基金涨跌幅 pass')
        except Exception as e:
            print('债券固收市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('债券固收市场沪深300涨跌幅 pass')
        except Exception as e:
            print('债券固收市场沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 管理期货市场
        public.find_element('xpath=>//*[@id="incomeUl"]/li[3]').click()  # 点击管理期货市场
        time.sleep(3)
        # 断言，管理期货市场基金涨跌幅
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('管理期货市场基金涨跌幅 pass')
        except Exception as e:
            print('管理期货市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金涨跌幅沪深300涨跌幅
        error_mes = public.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('基金涨跌幅沪深300涨跌幅 pass')
        except Exception as e:
            print('基金涨跌幅沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 市道分析
        public.execute_script_down()  # 浏览器往下
        time.sleep(3)
        # 断言，市道分析
        error_mes = public.find_element(
            'xpath=>//*[@id="market-main-table"]/tbody/tr[1]/td[2]').text  # 2.59%(151天)
        try:
            assert error_mes != u'--(-天)'
            print('市道分析 pass')
        except Exception as e:
            print('市道分析 fail', format(e))
            print(error_mes)
        time.sleep(5)
