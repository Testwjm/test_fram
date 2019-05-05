import time
from pageobjects.product_management import ProductManagement
from testsuites.my_test import MyTest


class TestProductManagement(MyTest):
    """产品管理"""

    def test_product_management_case1(self):
        """登录"""
        product = ProductManagement(self.driver)
        product.product_management_login()

    def test_product_management_case2(self):
        """列表"""
        product = ProductManagement(self.driver)
        product.product_management_list()
        # 断言，添加产品
        try:
            assert u"数据上传" in product.get_page_title()
            print('添加产品 pass')
        except Exception as e:
            print('添加产品 fail', format(e))
        time.sleep(2)
        product.back()
        time.sleep(5)
        # 断言，基金名称
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[1]/a').text
        try:
            assert error_mes != u'--'
            print('基金名称 pass')
        except Exception as e:
            print('基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，状态
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('状态 pass')
        except Exception as e:
            print('状态 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资策略
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，期初资产净值（万元）
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'--'
            print('期初资产净值（万元） pass')
        except Exception as e:
            print('期初资产净值（万元） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，期末资产净值（万元）
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('期末资产净值（万元） pass')
        except Exception as e:
            print('期末资产净值（万元） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间盈亏
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('区间盈亏 pass')
        except Exception as e:
            print('区间盈亏 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，自营资金占比
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes == u'--'
            print('自营资金占比 pass')
        except Exception as e:
            print('自营资金占比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，自营资金期间变化
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes == u'--'
            print('自营资金期间变化 pass')
        except Exception as e:
            print('自营资金期间变化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，敏感性指标
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[9]').text
        try:
            assert error_mes == u'--'
            print('敏感性指标 pass')
        except Exception as e:
            print('敏感性指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = product.find_element('xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[10]').text
        try:
            assert error_mes != u'--'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case3(self):
        """头部"""
        product = ProductManagement(self.driver)
        product.product_management_details()
        product.current_handel()
        time.sleep(2)
        # 断言，基金链接
        try:
            assert u"示例FOF母基金" in product.get_page_title()
            print('基金链接 pass')
        except Exception as e:
            print('基金链接 fail', format(e))
        time.sleep(2)
        # 断言，投资策略
        error_mes = product.find_element('xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes != u'--'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，代码
        error_mes = product.find_element('xpath=>//*[@id="reg_code"]').text
        try:
            assert error_mes != u'--'
            print('代码 pass')
        except Exception as e:
            print('代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指标日期
        error_mes = product.find_element('xpath=>//*[@id="prcInfo"]/div[1]/div[2]/div[1]/div[1]').text
        try:
            assert error_mes != u'--'
            print('指标日期 pass')
        except Exception as e:
            print('指标日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = product.find_element('xpath=>//*[@id="netNav"]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = product.find_element('xpath=>//*[@id="added_nav"]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = product.find_element('xpath=>//*[@id="swanav"]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指标日期
        error_mes = product.find_element('xpath=>//*[@id="prcInfo"]/div[1]/div[2]/div[2]/div[1]').text
        try:
            assert error_mes != u'--'
            print('指标日期 pass')
        except Exception as e:
            print('指标日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，今年以来收益率（月频）
        error_mes = product.find_element('xpath=>//*[@id="year_return"]').text
        try:
            assert error_mes != u'--'
            print('今年以来收益率（月频） pass')
        except Exception as e:
            print('今年以来收益率（月频） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立以来收益率（月频）
        error_mes = product.find_element('xpath=>//*[@id="total_return"]').text
        try:
            assert error_mes != u'--'
            print('成立以来收益率（月频） pass')
        except Exception as e:
            print('成立以来收益率（月频） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资顾问
        error_mes = product.find_element('xpath=>//*[@id="org_name"]').text
        try:
            assert error_mes != u'--'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = product.find_element('xpath=>//*[@id="foundation_date"]').text
        try:
            assert error_mes != u'--'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行状态
        error_mes = product.find_element('xpath=>//*[@id="fundStatu"]').text
        try:
            assert error_mes != u'--'
            print('运行状态 pass')
        except Exception as e:
            print('运行状态 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case4(self):
        """历史净值"""
        product = ProductManagement(self.driver)
        product.product_management_history()
        # 断言，净值日期
        error_mes = product.find_element('xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = product.find_element('xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = product.find_element('xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = product.find_element('xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case5(self):
        """同类排名"""
        product = ProductManagement(self.driver)
        product.product_management_rank()
        # 断言，年化收益率
        error_mes = product.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--\n（-）'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = product.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--\n（-）'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = product.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--\n（-）'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = product.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--\n（-）'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case6(self):
        """月频指标"""
        product = ProductManagement(self.driver)
        product.product_management_month_index()
        """收益指标"""
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品累计收益率 pass')
        except Exception as e:
            print('产品累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数累计收益率 pass')
        except Exception as e:
            print('股票多头策略指数累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        time.sleep(5)
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益率 pass')
        except Exception as e:
            print('产品收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益率 pass')
        except Exception as e:
            print('hs300收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数收益率 pass')
        except Exception as e:
            print('股票多头策略指数收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="incomeUl"]/li[1]').click()  # 点击累计收益率
        time.sleep(5)
        """风险指标"""
        # 断言，波动率
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，VaR
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        """动态回撤"""
        product.find_element('xpath=>//*[@id="showAll1"]').click()  # 点击显示全部
        time.sleep(5)
        """风险调整收益指标"""
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益指标
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益指标 pass')
        except Exception as e:
            print('产品收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益指标
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益指标 pass')
        except Exception as e:
            print('hs300收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数
        error_mes = product.find_element(
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
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case7(self):
        """周频指标"""
        product = ProductManagement(self.driver)
        product.refresh()
        time.sleep(5)
        product.current_handel()
        time.sleep(2)
        product.execute_script_in()
        time.sleep(2)
        product.product_management_week_index()
        """收益指标"""
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品累计收益率 pass')
        except Exception as e:
            print('产品累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数累计收益率 pass')
        except Exception as e:
            print('股票多头策略指数累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        time.sleep(5)
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益率 pass')
        except Exception as e:
            print('产品收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益率 pass')
        except Exception as e:
            print('hs300收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票多头策略指数收益率 pass')
        except Exception as e:
            print('股票多头策略指数收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="incomeUl"]/li[1]').click()  # 点击累计收益率
        time.sleep(5)
        """风险指标"""
        # 断言，波动率
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，VaR
        error_mes = product.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        """动态回撤"""
        product.find_element('xpath=>//*[@id="showAll1"]').click()  # 点击显示全部
        time.sleep(5)
        """风险调整收益指标"""
        # 断言，统计区间
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品收益指标
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('产品收益指标 pass')
        except Exception as e:
            print('产品收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300收益指标
        error_mes = product.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300收益指标 pass')
        except Exception as e:
            print('hs300收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票多头策略指数
        error_mes = product.find_element(
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
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = product.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case8(self):
        """基本信息"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 控制浏览器往上
        time.sleep(2)
        product.product_management_info()
        # 断言，基金简称
        error_mes = product.find_element(
            'xpath=>//*[@id="fundName"]').text
        try:
            assert error_mes == u'示例FOF母基金'
            print('基金简称 pass')
        except Exception as e:
            print('基金简称 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case9(self):
        """持仓分析"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 控制浏览器往上
        time.sleep(2)
        product.product_management_position()
        '''母基金配置'''
        # 断言，期初净资产
        error_mes = product.find_element('xpath=>//*[@id="parentfTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('期初净资产 pass')
        except Exception as e:
            print('期初净资产 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="parentFund"]/div[4]/div[1]/div/button[2]').click()  # 点击VaR贡献占比
        time.sleep(3)
        product.find_element('xpath=>//*[@id="parentFund"]/div[4]/div[1]/div/button[3]').click()  # 点击波动率贡献占比
        time.sleep(3)
        # 断言，收益贡献占比
        error_mes = product.find_element('xpath=>//*[@id="parentFund"]/div[3]/div[1]/div/span').text
        try:
            assert error_mes == u'收益贡献占比'
            print('收益贡献占比 pass')
        except Exception as e:
            print('收益贡献占比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，子基金组合时序图
        error_mes = product.find_element('xpath=>//*[@id="parentFund"]/div[5]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'子基金组合时序图'
            print('子基金组合时序图 pass')
        except Exception as e:
            print('子基金组合时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''策略配置'''
        # 断言，期末净资产
        error_mes = product.find_element('xpath=>//*[@id="policyTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('期末净资产 pass')
        except Exception as e:
            print('期末净资产 fail', format(e))
            print(error_mes)
        time.sleep(2)
        product.find_element('xpath=>//*[@id="policyChart"]/div[2]/div[1]/div/button[2]').click()  # 点击VaR贡献占比
        time.sleep(3)
        product.find_element('xpath=>//*[@id="policyChart"]/div[2]/div[1]/div/button[3]').click()  # 点击波动率贡献占比
        time.sleep(3)
        # 断言，收益贡献占比2
        error_mes = product.find_element('xpath=>//*[@id="policyChart"]/div[1]/div[1]/div/span').text
        try:
            assert error_mes == u'收益贡献占比'
            print('收益贡献占比2 pass')
        except Exception as e:
            print('收益贡献占比2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，子策略组合时序图
        error_mes = product.find_element('xpath=>//*[@id="policyChart"]/div[3]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'子策略组合时序图'
            print('子策略组合时序图 pass')
        except Exception as e:
            print('子策略组合时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''策略相关性'''
        # 断言，基金与指数滚动相关系数
        error_mes = product.find_element('xpath=>//*[@id="headtMapdiv"]/div[1]/span').text
        try:
            assert error_mes == u'基金与指数滚动相关系数'
            print('基金与指数滚动相关系数 pass')
        except Exception as e:
            print('基金与指数滚动相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 市场指数
        product.find_element('xpath=>//*[@id="HS300"]').click()  # 点击沪深300
        time.sleep(3)
        product.find_element('xpath=>//*[@id="nanhuaShop"]').click()  # 点击南华商品
        time.sleep(3)
        # 策略指数
        product.find_element('xpath=>//*[@id="allMark"]').click()  # 点击私募全市场
        time.sleep(3)
        product.find_element('xpath=>//*[@id="portfolioInvestment"]').click()  # 点击组合策略指数
        time.sleep(3)
        # 子基金相关系数
        # 断言，子基金相关系数
        error_mes = product.find_element('xpath=>//*[@id="policyDependencies"]/div[3]/div[1]/span').text
        try:
            assert error_mes == u'子基金相关系数'
            print('子基金相关系数 pass')
        except Exception as e:
            print('子基金相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 统计区间
        product.find_element('xpath=>//*[@id="m6"]').click()  # 点击6M
        time.sleep(3)

    def test_product_management_case91(self):
        """持仓分析-资产账户"""
        product = ProductManagement(self.driver)
        product.product_management_account()
        # 断言，资产账户
        error_mes = product.find_element('xpath=>//*[@id="assetAccounttbl"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'示例FOF母基金'
            print('资产账户 pass')
        except Exception as e:
            print('资产账户 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，资产净值（万元）
        error_mes = product.find_element('xpath=>//*[@id="assetAccounttbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('资产净值（万元） pass')
        except Exception as e:
            print('资产净值（万元） fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，占资产比例
        error_mes = product.find_element('xpath=>//*[@id="assetAccounttbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('占资产比例 pass')
        except Exception as e:
            print('占资产比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，占比区间变化
        error_mes = product.find_element('xpath=>//*[@id="assetAccounttbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('占比区间变化 pass')
        except Exception as e:
            print('占比区间变化 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case92(self):
        """持仓分析-股票资产"""
        product = ProductManagement(self.driver)
        product.product_management_shares()
        # 断言，行业分析资产净值
        error_mes = product.find_element('xpath=>//*[@id="stockIndustryTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('行业分析资产净值 pass')
        except Exception as e:
            print('行业分析资产净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，市值分析资产净值
        error_mes = product.find_element('xpath=>//*[@id="stockMarketValueTab"]/tbody/tr[4]/td[2]').text  # 300亿以上
        try:
            assert error_mes != u'--'
            print('市值分析资产净值 pass')
        except Exception as e:
            print('市值分析资产净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票分析资产净值
        error_mes = product.find_element('xpath=>//*[@id="stockAnalysisValuationTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('股票分析资产净值 pass')
        except Exception as e:
            print('股票分析资产净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，组合风险VaR
        error_mes = product.find_element('xpath=>//*[@id="95_1_2"]').text
        try:
            assert error_mes != u'--'
            print('组合风险VaR pass')
        except Exception as e:
            print('组合风险VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，交易行为分析
        error_mes = product.find_element('xpath=>//*[@id="stockAnalysisTransactions"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'0'
            print('交易行为分析 pass')
        except Exception as e:
            print('交易行为分析 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case93(self):
        """持仓分析-期货资产"""
        product = ProductManagement(self.driver)
        product.product_management_futures()
        # 断言，账户概况累计收益率
        error_mes = product.find_element(
            'xpath=>//*[@id="futuresAssets"]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('账户概况累计收益率 pass')
        except Exception as e:
            print('账户概况累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，账户出入金分析逐日期初权益
        error_mes = product.find_element('xpath=>//*[@id="ukashDaytbl"]/tbody/tr[12]/td[2]').text
        try:
            assert error_mes != u'--'
            print('账户出入金分析逐日期初权益 pass')
        except Exception as e:
            print('账户出入金分析逐日期初权益 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，头寸分析净头寸
        error_mes = product.find_element('xpath=>//*[@id="PositionsTbl"]/tbody/tr/td[2]').text
        try:
            assert error_mes != u'--'
            print('头寸分析净头寸 pass')
        except Exception as e:
            print('头寸分析净头寸 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，盈亏分析总盈亏全部交易
        error_mes = product.find_element('xpath=>//*[@id="profitTbl1"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('盈亏分析总盈亏全部交易 pass')
        except Exception as e:
            print('盈亏分析总盈亏全部交易 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，交易盈亏交易手数实际交易
        error_mes = product.find_element('xpath=>//*[@id="profitTbl2"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('交易盈亏交易手数实际交易 pass')
        except Exception as e:
            print('交易盈亏交易手数实际交易 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，特色指标成交金额全部交易
        error_mes = product.find_element('xpath=>//*[@id="datalistTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('特色指标成交金额全部交易 pass')
        except Exception as e:
            print('特色指标成交金额全部交易 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，特色指标最大使用资金全部交易
        error_mes = product.find_element('xpath=>//*[@id="datalistTbl"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('特色指标最大使用资金全部交易 pass')
        except Exception as e:
            print('特色指标最大使用资金全部交易 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，品种分析盈利
        error_mes = product.find_element('xpath=>//*[@id="VarietyNighttbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('品种分析盈利 pass')
        except Exception as e:
            print('品种分析盈利 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case94(self):
        """持仓分析-债券资产"""
        product = ProductManagement(self.driver)
        product.product_management_bond()
        # 断言，券种分析金额
        error_mes = product.find_element('xpath=>//*[@id="couponSpeciesTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('券种分析金额 pass')
        except Exception as e:
            print('券种分析金额 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置时序图金额
        error_mes = product.find_element('xpath=>//*[@id="ratingAnalysistbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('配置时序图金额 pass')
        except Exception as e:
            print('配置时序图金额 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，集中度分析
        error_mes = product.find_element('xpath=>//*[@id="bondCentralized"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('集中度分析 pass')
        except Exception as e:
            print('集中度分析 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case95(self):
        """净值归因"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 浏览器往上
        time.sleep(2)
        product.product_management_attribution()
        # 断言，大类资产占比情况
        error_mes1 = product.find_element('xpath=>//*[@id="comment1"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes == u'从仓位模拟结果来看'
            print('大类资产占比情况 pass')
        except Exception as e:
            print('大类资产占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况
        error_mes1 = product.find_element('xpath=>//*[@id="comment2"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes == u'在风格配置方面'
            print('风格因子占比情况 pass')
        except Exception as e:
            print('风格因子占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，拟合优度
        error_mes1 = product.find_element('xpath=>//*[@id="halfComment"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes != u'回归结果显示'
            print('拟合优度 pass')
        except Exception as e:
            print('拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case96(self):
        """持仓归因-资产账户"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 控制浏览器往上
        time.sleep(2)
        product.product_management_attribution_account()
        product.find_element('xpath=>//*[@id="assetAccount"]/table/tbody/tr[3]/td[2]/button[3]').click()  # 点击中债指数
        time.sleep(3)
        product.find_element('xpath=>//*[@id="assetAccount"]/table/tbody/tr[5]/td/button[1]').click()  # 点击确定
        time.sleep(20)
        # 断言，中债指数
        error_mes = product.find_element('xpath=>//*[@id="tab-main-grid"]/thead/tr[1]/th[3]/div[1]').text
        try:
            assert error_mes == u'中债指数'
            print('中债指数 pass')
        except Exception as e:
            print('中债指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单期归因
        error_mes = product.find_element('xpath=>//*[@id="assetAccount"]/div[4]/div[2]/span').text
        try:
            assert error_mes == u'单期归因'
            print('单期归因 pass')
        except Exception as e:
            print('单期归因 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，归因分析
        error_mes = product.find_element('xpath=>//*[@id="assetAccount"]/div[7]/div[2]/span').text
        try:
            assert error_mes == u'归因分析'
            print('归因分析 pass')
        except Exception as e:
            print('归因分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，仓位控制图
        error_mes = product.find_element('xpath=>//*[@id="assetAccount"]/div[9]/div[2]/span').text
        try:
            assert error_mes == u'仓位控制图'
            print('仓位控制图 pass')
        except Exception as e:
            print('仓位控制图 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case97(self):
        """持仓归因-股票资产"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 浏览器往上
        time.sleep(2)
        product.product_management_attribution_shares()
        product.find_element('xpath=>//*[@id="stockAccount"]/table/tbody/tr[1]/td[2]/button[2]').click()  # 归因方式点击多期
        time.sleep(3)
        product.find_element('xpath=>//*[@id="stockAccount"]/table/tbody/tr[4]/td/button[1]').click()  # 点击确定
        time.sleep(10)
        # 断言，股票资产单期归因
        error_mes = product.find_element('xpath=>//*[@id="stockAccount"]/div[4]/div[2]/span').text
        try:
            assert error_mes == u'多期归因'
            print('股票资产单期归因 pass')
        except Exception as e:
            print('股票资产单期归因 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票资产归因分析
        error_mes = product.find_element('xpath=>//*[@id="stockAccount"]/div[7]/div[2]/span').text
        try:
            assert error_mes == u'归因分析'
            print('股票资产归因分析 pass')
        except Exception as e:
            print('股票资产归因分析 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，股票资产仓位控制图
        error_mes = product.find_element('xpath=>//*[@id="stockAccount"]/div[9]/div[2]/span').text
        try:
            assert error_mes == u'仓位控制图'
            print('股票资产仓位控制图 pass.')
        except Exception as e:
            print('股票资产仓位控制图 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case98(self):
        """持仓归因-期货资产"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 浏览器往上
        time.sleep(2)
        product.product_management_attribution_futures()
        # 归因分析
        # 断言，总体期货绩效归因
        error_mes = product.find_element('xpath=>//*[@id="futuresOverallAttributionTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('总体期货绩效归因 pass')
        except Exception as e:
            print('总体期货绩效归因 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 品种归因分析
        # 断言，十大盈利
        error_mes = product.find_element('xpath=>//*[@id="futuresInterestContractTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('十大盈利 pass')
        except Exception as e:
            print('十大盈利 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，十大亏损
        error_mes = product.find_element('xpath=>//*[@id="futuresLossContractTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('十大亏损 pass')
        except Exception as e:
            print('十大亏损 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_product_management_case99(self):
        """情景分析"""
        product = ProductManagement(self.driver)
        product.execute_script_up()  # 浏览器往上
        time.sleep(2)
        product.product_management_scene()
        '''压力测试'''
        product.find_element('xpath=>//*[@id="incomeUl"]/li[3]').click()  # 点击管理期货市场
        time.sleep(5)
        # 断言，基金涨跌幅
        error_mes = product.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr/td[3]').text
        try:
            assert error_mes == u'--'
            print('基金涨跌幅 pass')
        except Exception as e:
            print('基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，沪深300涨跌幅
        error_mes = product.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr/td[4]').text
        try:
            assert error_mes == u'--'
            print('沪深300涨跌幅 pass')
        except Exception as e:
            print('沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''市道分析'''
        # 市道分析
        product.execute_script_down()  # 浏览器往下
        time.sleep(3)
        # 断言，市道分析
        error_mes = product.find_element(
            'xpath=>//*[@id="market-main-table"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--(0周)'
            print('市道分析 pass')
        except Exception as e:
            print('市道分析 fail', format(e))
            print(error_mes)
        time.sleep(5)
