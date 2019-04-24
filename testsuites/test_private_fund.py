import time
from pageobjects.private_fund import PrivateFund
from testsuites.MyTest import MyTest


class TestPrivateFund(MyTest):
    """私募基金详情页"""

    def test_private_fund_case1(self):
        """登录"""
        private = PrivateFund(self.driver)
        private.private_fund_login()

    def test_private_fund_case2(self):
        """头部"""
        private = PrivateFund(self.driver)
        private.private_fund_detail()
        private.current_handel()
        time.sleep(2)
        # 断言，详情页
        try:
            assert u"鹏华资产-清水源" in private.get_page_title()
            print('私募基金详情 pass')
        except Exception as e:
            print('私募基金详情 fail', format(e))
        time.sleep(2)
        # 断言，策略
        error_mes = private.find_element(
            'xpath=>//*[@id="Policy"]').text  # 股票策略-股票多头
        try:
            assert error_mes == u'股票策略-股票多头'
            print('策略 pass')
        except Exception as e:
            print('策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，代码
        error_mes = private.find_element(
            'xpath=>//*[@id="reg_code"]').text  # (SC7525)
        try:
            assert error_mes == u'(SC7525)'
            print('代码 pass')
        except Exception as e:
            print('代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，高风险(R4)
        error_mes = private.find_element(
            'xpath=>//*[@id="prcInfo"]/div[1]/div[1]/div[2]/div[2]/span[2]').text
        try:
            assert error_mes == u'高风险(R5)'
            print('高风险(R5) pass')
        except Exception as e:
            print('高风险(R5) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，星级
        error_mes = private.find_element(
            'xpath=>//*[@id="star"]').text
        try:
            assert error_mes == u''
            print('星级 pass')
        except Exception as e:
            print('星级 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = private.find_element(
            'xpath=>//*[@id="nav_date"]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = private.find_element(
            'xpath=>//*[@id="netNav"]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = private.find_element(
            'xpath=>//*[@id="added_nav"]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = private.find_element(
            'xpath=>//*[@id="swanav"]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指标日期
        error_mes = private.find_element(
            'xpath=>//*[@id="statistic_date"]').text
        try:
            assert error_mes != u'--'
            print('指标日期 pass')
        except Exception as e:
            print('指标日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，今年以来收益率（月频）
        error_mes = private.find_element(
            'xpath=>//*[@id="year_return"]').text
        try:
            assert error_mes != u'--'
            print('今年以来收益率（月频） pass')
        except Exception as e:
            print('今年以来收益率（月频） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立以来收益率（月频）
        error_mes = private.find_element(
            'xpath=>//*[@id="total_return"]').text
        try:
            assert error_mes != u'--'
            print('成立以来收益率（月频） pass')
        except Exception as e:
            print('成立以来收益率（月频） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资顾问
        error_mes = private.find_element(
            'xpath=>//*[@id="org_name"]').text  # 深圳清水源投资
        try:
            assert error_mes == u'深圳清水源投资'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金经理
        error_mes = private.find_element(
            'xpath=>//*[@id="fundManeger"]/a[1]').text
        try:
            assert error_mes == u'王韧'
            print('基金经理 pass')
        except Exception as e:
            print('基金经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = private.find_element(
            'xpath=>//*[@id="foundation_date"]').text  # 2014-09-30
        try:
            assert error_mes == u'2014-09-30'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行状态
        error_mes = private.find_element(
            'xpath=>//*[@id="fundStatu"]').text  # 运行中
        try:
            assert error_mes == u'运行中'
            print('运行状态 pass')
        except Exception as e:
            print('运行状态 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="org_name"]').click()  # 点击投顾链接
        time.sleep(5)
        private.current_handel()
        time.sleep(2)
        # 断言，投顾链接
        try:
            assert u"深圳清水源投资" in private.get_page_title()
            print('投顾链接 pass')
        except Exception as e:
            print('投顾链接 fail', format(e))
        time.sleep(2)
        private.back()  # 控制浏览器后退
        time.sleep(5)
        private.current_handel()
        time.sleep(2)
        private.find_element('xpath=>//*[@id="fundManeger"]/a[1]').click()  # 基金经理链接
        time.sleep(5)
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

    def test_private_fund_case3(self):
        """历史净值"""
        private = PrivateFund(self.driver)
        private.private_fund_history()
        # 断言，净值日期
        error_mes = private.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = private.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = private.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = private.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，数据来源
        error_mes = private.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('数据来源 pass')
        except Exception as e:
            print('数据来源 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_fund_case4(self):
        """同类排名"""
        private = PrivateFund(self.driver)
        private.private_fund_rank()
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

    def test_private_fund_case5(self):
        """月频指标"""
        private = PrivateFund(self.driver)
        private.private_fund_month_index()
        """收益指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品累计收益率 pass')
        except Exception as e:
            print('产品累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数累计收益率 pass')
        except Exception as e:
            print('股票多头策略指数累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        time.sleep(5)
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益率 pass')
        except Exception as e:
            print('产品收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益率 pass')
        except Exception as e:
            print('hs300收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数收益率 pass')
        except Exception as e:
            print('股票多头策略指数收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="incomeUl"]/li[1]').click()  # 点击累计收益率
        time.sleep(5)
        """风险指标"""
        # 断言，波动率
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，VaR
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        """动态回撤"""
        private.find_element('xpath=>//*[@id="showAll1"]').click()  # 点击显示全部
        time.sleep(5)
        """风险调整收益指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益指标
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益指标 pass')
        except Exception as e:
            print('产品收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益指标
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益指标 pass')
        except Exception as e:
            print('hs300收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数 pass')
        except Exception as e:
            print('股票多头策略指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        """相对指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_fund_case6(self):
        """周频指标"""
        private = PrivateFund(self.driver)
        private.refresh()
        time.sleep(5)
        private.current_handel()
        time.sleep(2)
        private.execute_script_in()
        time.sleep(2)
        private.private_fund_week_index()
        """收益指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品累计收益率 pass')
        except Exception as e:
            print('产品累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数累计收益率 pass')
        except Exception as e:
            print('股票多头策略指数累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        time.sleep(5)
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益率 pass')
        except Exception as e:
            print('产品收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益率 pass')
        except Exception as e:
            print('hs300收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数收益率 pass')
        except Exception as e:
            print('股票多头策略指数收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="incomeUl"]/li[1]').click()  # 点击累计收益率
        time.sleep(5)
        """风险指标"""
        # 断言，波动率
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，VaR
        error_mes = private.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        """动态回撤"""
        private.find_element('xpath=>//*[@id="showAll1"]').click()  # 点击显示全部
        time.sleep(5)
        """风险调整收益指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益指标
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益指标 pass')
        except Exception as e:
            print('产品收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益指标
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益指标 pass')
        except Exception as e:
            print('hs300收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数
        error_mes = private.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数 pass')
        except Exception as e:
            print('股票多头策略指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        """相对指标"""
        # 断言，统计区间
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = private.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_fund_case7(self):
        """净值归因"""
        private = PrivateFund(self.driver)
        private.execute_script_up()
        time.sleep(2)
        private.private_fund_nv()
        '''夏普模型'''
        # 断言，大类资产占比情况
        error_mes = private.find_element(
            'xpath=>//*[@id="tab2"]/div[2]/div[1]/span').text  # 大类资产占比情况
        try:
            assert error_mes == u'大类资产占比情况'
            print('大类资产占比情况 pass')
        except Exception as e:
            print('大类资产占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = private.find_element('xpath=>//*[@id="comment1"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        # 断言，大类资产占比情况语句
        error_mes = one
        try:
            assert error_mes == u'从仓位模拟结果来看'
            print('大类资产占比情况语句 pass')
        except Exception as e:
            print('大类资产占比情况语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况
        error_mes = private.find_element(
            'xpath=>//*[@id="tab2"]/div[3]/div[1]/span').text  # 风格因子占比情况
        try:
            assert error_mes == u'风格因子占比情况'
            print('风格因子占比情况 pass')
        except Exception as e:
            print('风格因子占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况语句
        one = private.find_element('xpath=>//*[@id="comment2"]').text
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
        one = private.find_element('xpath=>//*[@id="halfComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        # 断言，大类资产拟合优度语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('大类资产拟合优度语句 pass')
        except Exception as e:
            print('大类资产拟合优度语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('大类资产 pass')
        except Exception as e:
            print('大类资产 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('风格因子 pass')
        except Exception as e:
            print('风格因子 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产权重
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[3]').text  # 权重
        try:
            assert error_mes != u'--'
            print('大类资产权重 pass')
        except Exception as e:
            print('大类资产权重 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产P值
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[4]').text  # P值
        try:
            assert error_mes != u'--'
            print('大类资产P值 pass')
        except Exception as e:
            print('大类资产P值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，显著标记
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes == u'--'
            print('显著标记 pass')
        except Exception as e:
            print('显著标记 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产收益贡献率
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[6]').text  # 收益贡献率
        try:
            assert error_mes != u'--'
            print('大类资产收益贡献率 pass')
        except Exception as e:
            print('大类资产收益贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，大类资产波动贡献率
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid1"]/tbody/tr[1]/td[7]').text  # 波动贡献率
        try:
            assert error_mes != u'--'
            print('大类资产波动贡献率 pass')
        except Exception as e:
            print('大类资产波动贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格变化
        error_mes = private.find_element(
            'xpath=>//*[@id="tab2"]/div[5]/div[1]/div/div[2]/span').text  # 风格变化
        try:
            assert error_mes == u'风格变化'
            print('风格变化 pass')
        except Exception as e:
            print('风格变化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益分解时序图
        error_mes = private.find_element(
            'xpath=>//*[@id="tab2"]/div[6]/div[1]/div[1]/div/span').text  # 收益分解时序图
        try:
            assert error_mes == u'收益分解时序图'
            print('收益分解时序图 pass')
        except Exception as e:
            print('收益分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风险分解时序图
        error_mes = private.find_element(
            'xpath=>//*[@id="tab2"]/div[6]/div[2]/div[1]/div/span').text  # 风险分解时序图
        try:
            assert error_mes == u'风险分解时序图'
            print('风险分解时序图 pass')
        except Exception as e:
            print('风险分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，行业模拟
        error_mes = private.find_element(
            'xpath=>//*[@id="simulation"]/div[1]/div[2]/span[1]').text  # 行业模拟
        try:
            assert error_mes == u'行业模拟'
            print('行业模拟 pass')
        except Exception as e:
            print('行业模拟 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = private.find_element('xpath=>//*[@id="mnComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        # 断言，行业模拟语句
        error_mes = one
        try:
            assert error_mes == u'从行业模拟结果来看'
            print('行业模拟语句 pass')
        except Exception as e:
            print('行业模拟语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = private.find_element('xpath=>//*[@id="halfComment2"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        # 断言，行业拟合优度语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('行业拟合优度语句 pass')
        except Exception as e:
            print('行业拟合优度语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，行业
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('行业 pass')
        except Exception as e:
            print('行业 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，权重
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('权重 pass')
        except Exception as e:
            print('权重 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，P值
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('P值 pass')
        except Exception as e:
            print('P值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，显著标记
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'--'
            print('显著标记 pass')
        except Exception as e:
            print('显著标记 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益贡献率
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('收益贡献率 pass')
        except Exception as e:
            print('收益贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，波动贡献率
        error_mes = private.find_element(
            'xpath=>//*[@id="main-grid2"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('波动贡献率 pass')
        except Exception as e:
            print('波动贡献率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，行业变化
        error_mes = private.find_element(
            'xpath=>//*[@id="isShow"]/div[1]/div[1]/div/div[2]/span').text
        try:
            assert error_mes == u'行业变化'
            print('行业变化 pass')
        except Exception as e:
            print('行业变化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，收益分解时序图
        error_mes = private.find_element(
            'xpath=>//*[@id="isShow"]/div[2]/div[1]/div[1]/div/span').text
        try:
            assert error_mes == u'收益分解时序图'
            print('收益分解时序图 pass')
        except Exception as e:
            print('收益分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，波动分解时序图
        error_mes = private.find_element(
            'xpath=>//*[@id="isShow"]/div[2]/div[2]/div[1]/div/span').text
        try:
            assert error_mes == u'波动分解时序图'
            print('波动分解时序图 pass')
        except Exception as e:
            print('波动分解时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_fund_case8(self):
        """FF模型"""
        private = PrivateFund(self.driver)
        private.private_fund_ff()
        # 三因子收益贡献分解
        # 断言三因子收益贡献分解
        error_mes = private.find_element(
            'xpath=>//*[@id="tab3"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('三因子收益贡献分解 pass')
        except Exception as e:
            print('三因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子收益贡献分解语句
        one = private.find_element('xpath=>//*[@id="incomeComent"]').text
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
        error_mes = private.find_element(
            'xpath=>//*[@id="tab3"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('三因子风险贡献分解 pass')
        except Exception as e:
            print('三因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子风险贡献分解语句
        one = private.find_element('xpath=>//*[@id="riskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前面的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('三因子风险贡献分解语句 pass')
        except Exception as e:
            print('三因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 三因子因子相关性
        # 断言，三因子因子相关性
        error_mes = private.find_element(
            'xpath=>//*[@id="tab3"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes == u'因子相关性'
            print('三因子因子相关性 pass')
        except Exception as e:
            print('三因子因子相关性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子相关性语句1
        one = private.find_element('xpath=>//*[@id="yzComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('三因子因子相关性语句1 pass')
        except Exception as e:
            print('三因子因子相关性语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子相关性语句2
        one = private.find_element('xpath=>//*[@id="yzComment2"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'因子之间的相关性较低'
            print('三因子因子相关性语句2 pass')
        except Exception as e:
            print('三因子因子相关性语句2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子系数
        error_mes = private.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('三因子因子系数 pass')
        except Exception as e:
            print('三因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子因子系数值
        error_mes = private.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('三因子因子系数值 pass')
        except Exception as e:
            print('三因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子p值
        error_mes = private.find_element(
            'xpath=>//*[@id="fit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('三因子p值 pass')
        except Exception as e:
            print('三因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，三因子拟合优度
        error_mes = private.find_element(
            'xpath=>//*[@id="r_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('三因子拟合优度 pass')
        except Exception as e:
            print('三因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        private.execute_script_up()  # 浏览器往上
        time.sleep(3)
        '''Carhart四因子'''
        private.find_element('xpath=>//*[@id="tab1"]/div[1]/label[2]').click()  # 点击Carhart四因子
        time.sleep(10)
        # 四因子收益贡献分解
        # 断言，四因子收益贡献分解
        error_mes = private.find_element(
            'xpath=>//*[@id="tab4"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('四因子收益贡献分解 pass')
        except Exception as e:
            print('四因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子收益贡献分解语句
        one = private.find_element('xpath=>//*[@id="income-comment4"]').text
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
        error_mes = private.find_element(
            'xpath=>//*[@id="tab4"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('四因子风险贡献分解 pass')
        except Exception as e:
            print('四因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子风险贡献分解语句
        one = private.find_element(
            'xpath=>//*[@id="fourriskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('四因子风险贡献分解语句 pass')
        except Exception as e:
            print('四因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 四因子因子暴露及相关性分析
        # 断言，四因子因子暴露及相关性分析
        error_mes = private.find_element(
            'xpath=>//*[@id="tab4"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes == u'因子暴露及相关性分析'
            print('四因子因子暴露及相关性分析 pass')
        except Exception as e:
            print('四因子因子暴露及相关性分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子暴露及相关性分析语句1
        one = private.find_element('xpath=>//*[@id="fouryzComment"]').text
        one = one.split('，')[0]  # 获取这句话逗号前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果显示'
            print('四因子因子暴露及相关性分析语句1 pass.')
        except Exception as e:
            print('四因子因子暴露及相关性分析语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子暴露及相关性分析语句2
        private.find_element('xpath=>//*[@id="fouryzComment2"]').text
        one = one.split('显')[0]  # 获取这句话显前的语句
        error_mes = one
        try:
            assert error_mes == u'回归结果'
            print('四因子因子暴露及相关性分析语句2 pass.')
        except Exception as e:
            print('四因子因子暴露及相关性分析语句2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子系数
        error_mes = private.find_element(
            'xpath=>//*[@id="fouryzComment2"]').text
        try:
            assert error_mes != u'--'
            print('四因子因子系数 pass.')
        except Exception as e:
            print('四因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子因子系数值
        error_mes = private.find_element(
            'xpath=>//*[@id="fourfit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('四因子因子系数值 pass')
        except Exception as e:
            print('四因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子p值
        error_mes = private.find_element(
            'xpath=>//*[@id="fourfit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('四因子p值 pass')
        except Exception as e:
            print('四因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，四因子拟合优度
        error_mes = private.find_element(
            'xpath=>//*[@id="fourr_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('四因子拟合优度 pass')
        except Exception as e:
            print('四因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        private.execute_script_up()  # 浏览器往上
        time.sleep(3)
        '''FF五因子'''
        private.find_element('xpath=>//*[@id="tab1"]/div[1]/label[3]').click()  # 点击FF五因子
        time.sleep(10)
        # 五因子收益贡献分解
        # 断言，五因子收益贡献分解
        error_mes = private.find_element(
            'xpath=>//*[@id="tab5"]/div[1]/div[2]/span[1]').text
        try:
            assert error_mes == u'收益贡献分解'
            print('五因子收益贡献分解 pass')
        except Exception as e:
            print('五因子收益贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子收益贡献分解语句
        one = private.find_element('xpath=>//*[@id="incomeComent2"]').text
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
        error_mes = private.find_element(
            'xpath=>//*[@id="tab5"]/div[5]/div[2]/span[1]').text
        try:
            assert error_mes == u'风险贡献分解'
            print('五因子风险贡献分解 pass')
        except Exception as e:
            print('五因子风险贡献分解 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子风险贡献分解语句
        one = private.find_element('xpath=>//*[@id="fiveriskComment"]').text
        one = one.split('金')[0]  # 获取这句话金前的语句
        error_mes = one
        try:
            assert error_mes == u'该基'
            print('五因子风险贡献分解语句 pass')
        except Exception as e:
            print('五因子风险贡献分解语句 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 因子暴露及相关性分析
        # 断言，五因子因子暴露及相关性分析
        error_mes = private.find_element(
            'xpath=>//*[@id="tab5"]/div[9]/div[2]/span[1]').text
        try:
            assert error_mes == u'因子暴露及相关性分析'
            print('五因子因子暴露及相关性分析 pass')
        except Exception as e:
            print('五因子因子暴露及相关性分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子暴露及相关性分析语句1
        one = private.find_element('xpath=>//*[@id="fiveyzComment2"]').text
        one = one.split('间')[0]  # 获取这句话间前的语句
        error_mes = one
        try:
            assert error_mes == u'因子之'
            print('五因子因子暴露及相关性分析语句1 pass')
        except Exception as e:
            print('五因子因子暴露及相关性分析语句1 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子暴露及相关性分析语句2
        one = private.find_element('xpath=>//*[@id="fiveyzComment"]').text
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
        error_mes = private.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('五因子因子系数 pass')
        except Exception as e:
            print('五因子因子系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子因子系数值
        error_mes = private.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('五因子因子系数值 pass')
        except Exception as e:
            print('五因子因子系数值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子p值
        error_mes = private.find_element(
            'xpath=>//*[@id="fivefit"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('五因子p值 pass')
        except Exception as e:
            print('五因子p值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，五因子拟合优度
        error_mes = private.find_element(
            'xpath=>//*[@id="fiver_square"]').text  # 拟合优度
        try:
            assert error_mes != u'--'
            print('五因子拟合优度 pass')
        except Exception as e:
            print('五因子拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 控制浏览器到最上面
        private.execute_script_up()  # 浏览器往上
        time.sleep(3)

    def test_private_fund_case9(self):
        """Barra模型"""
        private = PrivateFund(self.driver)
        private.private_fund_barra()
        # 断言，因子
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'市值'
            print('因子 pass')
        except Exception as e:
            print('因子 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化方差
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('年化方差 pass')
        except Exception as e:
            print('年化方差 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，因子暴露
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('因子暴露 pass')
        except Exception as e:
            print('因子暴露 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，因子有效性
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('因子有效性 pass')
        except Exception as e:
            print('因子有效性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，择时有效性
        error_mes = private.find_element(
            'xpath=>//*[@id="barraTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('择时有效性 pass')
        except Exception as e:
            print('择时有效性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.find_element('xpath=>//*[@id="barra_bck"]/button[2]').click()  # 点击年化方差
        time.sleep(3)
        private.find_element('xpath=>//*[@id="barra_bck"]/button[3]').click()  # 点击因子暴露
        time.sleep(3)
        private.find_element('xpath=>//*[@id="barra_bck"]/button[4]').click()  # 点击有效性研判
        time.sleep(3)

    def test_private_fund_case91(self):
        """情景分析"""
        private = PrivateFund(self.driver)
        private.private_fund_scene()
        # 断言，事件
        error_mes = private.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[3]/td[1]').text
        try:
            assert error_mes == u'2019年年初原油价格大幅反弹'
            print('事件 pass')
        except Exception as e:
            print('事件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，日期范围
        error_mes = private.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes == u'2019-01-01 - 2019-01-31'
            print('日期范围 pass')
        except Exception as e:
            print('日期范围 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金涨跌幅
        error_mes = private.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[3]/td[3]').text
        try:
            assert error_mes != u'--'
            print('基金涨跌幅 pass')
        except Exception as e:
            print('基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300涨跌幅
        error_mes = private.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[3]/td[4]').text
        try:
            assert error_mes != u'--'
            print('hs300涨跌幅 pass')
        except Exception as e:
            print('hs300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''市场分析'''
        private.execute_script_down()
        time.sleep(2)
        # 断言，市道分析
        error_mes = private.find_element(
            'xpath=>//*[@id="SituationalAnalysis"]/div/div/div[3]/div[3]/span').text
        try:
            assert error_mes == u'市道分析'
            print('市道分析 pass')
        except Exception as e:
            print('市道分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，市道分析
        error_mes = private.find_element(
            'xpath=>//*[@id="market-main-table"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--(-周)'
            print('市道分析 pass')
        except Exception as e:
            print('市道分析 fail', format(e))
            print(error_mes)
        time.sleep(5)
