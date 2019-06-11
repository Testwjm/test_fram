import time
from pageobjects.strategy_budget_model import StrategyBudgetModel
from testsuites.my_test import MyTest


class TestStrategyBudgetModel(MyTest):
    """策略组合-风险预算模型"""

    def test_strategy_budget_case1(self):
        """登录"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_login()

    def test_strategy_budget_case2(self):
        """创建新的策略组合"""
        strategy = StrategyBudgetModel(self.driver)
        # 断言，创建产品组合
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[1]/div[2]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'创建策略组合'
            print('创建策略组合 pass')
        except Exception as e:
            print('创建策略组合 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.strategy_budget_establish()

    def test_strategy_budget_case3(self):
        """参数设置"""
        strategy = StrategyBudgetModel(self.driver)
        # 断言，参数设置
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbModel"]/div/div[2]/div[2]/span').text
        try:
            assert error_mes == u'参数设置'
            print('参数设置 pass')
        except Exception as e:
            print('参数设置 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，目标函数选择
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbModel"]/div/div[3]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'目标函数选择'
            print('目标函数选择 pass')
        except Exception as e:
            print('目标函数选择 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，选择约束条件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbModel"]/div/div[3]/div[2]/div[1]/span').text
        try:
            assert error_mes == u'选择约束条件'
            print('选择约束条件 pass')
        except Exception as e:
            print('选择约束条件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指数名称
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'私募全市场指数'
            print('指数名称 pass')
        except Exception as e:
            print('指数名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbTbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('区间年化收益率 pass')
        except Exception as e:
            print('区间年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbTbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('区间最大回撤 pass')
        except Exception as e:
            print('区间最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbTbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('区间年化夏普比 pass')
        except Exception as e:
            print('区间年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="rbTbl"]/tbody/tr[1]/td[6]').text
        try:

            assert error_mes != u'--'
            print('区间年化波动率 pass')
        except Exception as e:
            print('区间年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.strategy_budget_target()

    def test_strategy_budget_case4(self):
        """策略组合"""
        strategy = StrategyBudgetModel(self.driver)
        # 断言，Benchmark
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[2]/table/tbody/tr/td[1]/div[2]').text
        try:
            assert error_mes == u'沪深300,南华商品指数'
            print('Benchmark pass')
        except Exception as e:
            print('Benchmark fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置模式
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[2]/table/tbody/tr/td[2]/div[2]').text
        try:
            assert error_mes == u'风险预算模型'
            print('配置模式 pass')
        except Exception as e:
            print('配置模式 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，内外样本区间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[2]/table/tbody/tr/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('内外样本区间 pass')
        except Exception as e:
            print('内外样本区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，目标设定
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[2]/table/tbody/tr/td[4]/div[2]').text
        try:
            assert error_mes == u'资产风险贡献跟踪误差最小'
            print('目标设定 pass')
        except Exception as e:
            print('目标设定 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，全样本区间约束条件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskConditions"]').text
        try:
            assert error_mes == u'预期年化收益率 >= 2.00%,预期年化波动率 <= 5.00%'
            print('全样本区间约束条件 pass')
        except Exception as e:
            print('全样本区间约束条件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指数名称
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'私募全市场指数'
            print('指数名称 pass')
        except Exception as e:
            print('指数名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置比例
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[7]/span').text
        try:
            assert error_mes != u'--'
            print('配置比例 pass')
        except Exception as e:
            print('配置比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，拟投资金额（万元）
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskcreatPrctbl"]/tbody/tr[1]/td[8]/span').text
        try:
            assert error_mes != u'--'
            print('拟投资金额（万元) pass')
        except Exception as e:
            print('拟投资金额（万元) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，组合预期业绩指标
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/div/div/span').text
        try:
            assert error_mes == u'组合预期业绩指标'
            print('组合预期业绩指标 pass')
        except Exception as e:
            print('组合预期业绩指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[1]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[1]/td[2]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[1]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化下行标准差
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[2]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化下行标准差 pass')
        except Exception as e:
            print('年化下行标准差 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，Sortino比率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[2]/td[2]/div[2]').text
        try:
            assert error_mes != u'--'
            print('Sortino比率 pass')
        except Exception as e:
            print('Sortino比率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[2]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[3]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤发生时间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[3]/td[2]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤发生时间 pass')
        except Exception as e:
            print('最大回撤发生时间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤形成期
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskTbldiv"]/table/tbody/tr[3]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤形成期 pass')
        except Exception as e:
            print('最大回撤形成期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[5]/div[1]/div/div[1]/div/span').text
        try:
            assert error_mes == u'累计收益率'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，期间收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[6]/div/div[1]/div/span').text
        try:
            assert error_mes == u'期间收益率'
            print('期间收益率 pass')
        except Exception as e:
            print('期间收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，动态回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[9]/div[2]/div[7]/div/div[1]/div/span').text
        try:
            assert error_mes == u'动态回撤'
            print('动态回撤 pass')
        except Exception as e:
            print('动态回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.execute_script_down()
        time.sleep(2)
        strategy.strategy_budget_compose()

    def test_strategy_budget_case5(self):
        """头部"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_head()
        # 断言，投资策略
        error_mes = strategy.find_element(
            'xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes == u'组合策略-FOF'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，披露频率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="freq"]').text
        try:
            assert error_mes != u'--'
            print('披露频率 pass')
        except Exception as e:
            print('披露频率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = strategy.find_element(
            'xpath=>//*[@id="nav_date"]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = strategy.find_element(
            'xpath=>//*[@id="netNav"]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，今年以来收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="year_return"]').text
        try:
            assert error_mes != u'--'
            print('今年以来收益率 pass')
        except Exception as e:
            print('今年以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立以来收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="total_return"]').text
        try:
            assert error_mes != u'--'
            print('成立以来收益率 pass')
        except Exception as e:
            print('成立以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = strategy.find_element(
            'xpath=>//*[@id="foundation_date"]').text
        try:
            assert error_mes != u'--'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置模型
        error_mes = strategy.find_element(
            'xpath=>//*[@id="modalStyle"]').text
        try:
            assert error_mes == u'风险预算模型'
            print('配置模型 pass')
        except Exception as e:
            print('配置模型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，既定目标
        error_mes = strategy.find_element(
            'xpath=>//*[@id="target"]').text
        try:
            assert error_mes == u'资产风险贡献跟踪误差最小'
            print('既定目标 pass')
        except Exception as e:
            print('既定目标 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case6(self):
        """历史净值"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_history()
        # 断言，净值日期
        error_mes = strategy.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = strategy.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = strategy.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，复权累计净值
        error_mes = strategy.find_element(
            'xpath=>//*[@id="nav-main-grid"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('复权累计净值 pass')
        except Exception as e:
            print('复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case7(self):
        """指标"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_index()
        '''收益指标'''
        # 断言，统计区间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金累计收益率 pass')
        except Exception as e:
            print('基金累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('hs300累计收益率 pass')
        except Exception as e:
            print('hs300累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击年化收益率
        # 断言，统计区间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="incomeIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金年化收益率 pass')
        except Exception as e:
            print('基金年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300年化收益率
        error_mes = strategy.find_element(
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
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('VaR pass')
        except Exception as e:
            print('VaR fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[3]/td[2]').text
        try:
            assert error_mes != u'--'
            print('波动率 pass')
        except Exception as e:
            print('波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskIndicatorsTab"]/tbody/tr[4]/td[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''动态回撤'''
        strategy.find_element('xpath=>//*[@id="showAll1"]').click()
        time.sleep(5)
        '''风险调整收益指标'''
        # 断言，统计区间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金风险调整收益指标
        error_mes = strategy.find_element(
            'xpath=>//*[@id="riskAdjustmentTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('基金风险调整收益指标 pass')
        except Exception as e:
            print('基金风险调整收益指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，hs300风险调整收益指标
        error_mes = strategy.find_element(
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
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'成立以来'
            print('统计区间 pass')
        except Exception as e:
            print('统计区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，胜率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('胜率 pass')
        except Exception as e:
            print('胜率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，相关系数
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('相关系数 pass')
        except Exception as e:
            print('相关系数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化信息比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化信息比 pass')
        except Exception as e:
            print('年化信息比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化詹森指数
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('年化詹森指数 pass')
        except Exception as e:
            print('年化詹森指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化特雷诺比率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="relativeIndexTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('年化特雷诺比率 pass')
        except Exception as e:
            print('年化特雷诺比率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case8(self):
        """持仓分析"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.execute_script_up()
        time.sleep(2)
        strategy.strategy_budget_position()
        '''策略配置'''
        # 断言，期初净资产
        error_mes = strategy.find_element('xpath=>//*[@id="policyTbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('期初净资产 pass')
        except Exception as e:
            print('期初净资产 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，资产占比
        error_mes = strategy.find_element('xpath=>//*[@id="policyChart"]/div[1]/div[1]/div/span').text
        try:
            assert error_mes == u'资产占比'
            print('资产占比 pass')
        except Exception as e:
            print('资产占比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.find_element('xpath=>//*[@id="policyChart"]/div[2]/div[1]/div/button[2]').click()  # 点击VaR贡献占比
        time.sleep(3)
        strategy.find_element('xpath=>//*[@id="policyChart"]/div[2]/div[1]/div/button[3]').click()  # 点击波动率贡献占比
        time.sleep(3)
        # 断言，子策略组合时序图
        error_mes = strategy.find_element('xpath=>//*[@id="policyChart"]/div[3]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'子策略组合时序图'
            print('子策略组合时序图 pass')
        except Exception as e:
            print('子策略组合时序图 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''策略相关性'''
        # 断言，策略相关性
        error_mes = strategy.find_element('xpath=>//*[@id="headtMapdiv"]/div[1]/span').text
        try:
            assert error_mes == u'基金与指数滚动相关系数'
            print('策略相关性 pass')
        except Exception as e:
            print('策略相关性 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 市场指数
        strategy.find_element('xpath=>//*[@id="HS300"]').click()  # 点击沪深300
        time.sleep(3)
        strategy.find_element('xpath=>//*[@id="nanhuaShop"]').click()  # 点击南华商品
        time.sleep(3)
        # 策略指数
        strategy.find_element('xpath=>//*[@id="allMark"]').click()  # 点击私募全市场
        time.sleep(3)
        strategy.find_element('xpath=>//*[@id="portfolioInvestment"]').click()  # 点击组合策略指数
        time.sleep(3)
        # 断言，策略相关性2
        error_mes = strategy.find_element('xpath=>//*[@id="policyDependencies"]/div[3]/div[1]/span').text
        try:
            assert error_mes == u'子基金相关系数'
            print('策略相关性2 pass')
        except Exception as e:
            print('策略相关性2 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 统计区间
        strategy.find_element('xpath=>//*[@id="y1"]').click()  # 点击1Y
        time.sleep(5)

    def test_strategy_budget_case9(self):
        """净值归因"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.execute_script_up()
        time.sleep(2)
        strategy.strategy_budget_attribution()
        # 断言，大类资产占比情况
        error_mes1 = strategy.find_element('xpath=>//*[@id="comment1"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes == u'从仓位模拟结果来看'
            print('大类资产占比情况 pass')
        except Exception as e:
            print('大类资产占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，风格因子占比情况
        error_mes1 = strategy.find_element('xpath=>//*[@id="comment2"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes == u'在风格配置方面'
            print('风格因子占比情况 pass')
        except Exception as e:
            print('风格因子占比情况 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，拟合优度
        error_mes1 = strategy.find_element('xpath=>//*[@id="halfComment"]').text
        error_mes = error_mes1.split('，')[0]
        try:
            assert error_mes == u'回归结果显示'
            print('拟合优度 pass')
        except Exception as e:
            print('拟合优度 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case91(self):
        """情景分析"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.execute_script_up()
        time.sleep(2)
        strategy.strategy_budget_scene()
        '''压力测试'''
        # 断言，A股市场事件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[1]').text
        try:
            assert error_mes != u'--'
            print('A股市场事件 pass')
        except Exception as e:
            print('A股市场事件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，A股市场日期范围
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes != u'--'
            print('A股市场日期范围 pass')
        except Exception as e:
            print('A股市场日期范围 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，A股市场基金涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[3]').text
        try:
            assert error_mes != u'--'
            print('A股市场基金涨跌幅 pass')
        except Exception as e:
            print('A股市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，A股市场沪深300涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[4]').text
        try:
            assert error_mes != u'--'
            print('A股市场沪深300涨跌幅 pass')
        except Exception as e:
            print('A股市场沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 债券固收市场
        strategy.find_element('xpath=>//*[@id="incomeUl"]/li[2]').click()  # 点击债券固收市场
        time.sleep(3)
        # 断言，债券固收市场事件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[1]').text
        try:
            assert error_mes == u'土耳其货币危机'
            print('债券固收市场事件 pass')
        except Exception as e:
            print('债券固收市场事件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，债券固收市场日期范围
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[2]').text
        try:
            assert error_mes == u'2018-08-10 - 2018-08-18'
            print('债券固收市场日期范围 pass')
        except Exception as e:
            print('债券固收市场日期范围 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，债券固收市场基金涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[3]').text
        try:
            assert error_mes != u'--'
            print('债券固收市场基金涨跌幅 pass')
        except Exception as e:
            print('债券固收市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，债券固收市场沪深300涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[2]/td[4]').text
        try:
            assert error_mes != u'--'
            print('债券固收市场沪深300涨跌幅 pass')
        except Exception as e:
            print('债券固收市场沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 管理期货市场
        strategy.find_element('xpath=>//*[@id="incomeUl"]/li[3]').click()  # 点击管理期货市场
        time.sleep(3)
        # 断言，管理期货市场事件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'2018黑色系牛市'
            print('管理期货市场事件 pass')
        except Exception as e:
            print('管理期货市场事件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，管理期货市场日期范围
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'2018-07-26 - 2018-08-20'
            print('管理期货市场日期范围 pass')
        except Exception as e:
            print('管理期货市场日期范围 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，管理期货市场基金涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('管理期货市场基金涨跌幅 pass')
        except Exception as e:
            print('管理期货市场基金涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金涨跌幅沪深300涨跌幅
        error_mes = strategy.find_element(
            'xpath=>//*[@id="stressTestTab"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('基金涨跌幅沪深300涨跌幅 pass')
        except Exception as e:
            print('基金涨跌幅沪深300涨跌幅 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''市道分析'''
        # 市道分析
        strategy.execute_script_down()  # 浏览器往下
        time.sleep(3)
        # 断言，市道分析
        error_mes = strategy.find_element(
            'xpath=>//*[@id="market-main-table"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--(0周)'
            print('市道分析 pass')
        except Exception as e:
            print('市道分析 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case92(self):
        """删除"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_delete()
        # 断言，删除产品
        error_mes = strategy.find_element(
            'xpath=>//*[@id="policyCom"]/ul/li[1]/div[1]/a[1]/span').text
        try:
            assert error_mes != u'--'
            print('删除产品 pass')
        except Exception as e:
            print('删除产品 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_strategy_budget_case93(self):
        """指数"""
        strategy = StrategyBudgetModel(self.driver)
        strategy.strategy_budget_exponent()
        '''策略指数累计收益率'''
        # 断言，策略指数累计收益率
        error_mes = strategy.find_element('xpath=>//*[@id="policyCom"]/div[2]/div[3]/span').text
        try:
            assert error_mes == u'策略指数累计收益率'
            print('策略指数累计收益率 pass')
        except Exception as e:
            print('策略指数累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''指数相关性'''
        # 关注指数
        strategy.find_element('xpath=>//*[@id="FI12"]').click()  # 点击多策略指数
        time.sleep(5)
        # 断言，关注指数
        error_mes = strategy.find_element('xpath=>//*[@id="FI12"]').text
        try:
            assert error_mes == u'多策略指数'
            print('关注指数 pass')
        except Exception as e:
            print('关注指数 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # Benchmark
        strategy.find_element('xpath=>//*[@id="heatMapdiv"]/div[1]/div[2]/div/button[1]').click()  # 点击沪深300
        time.sleep(3)
        strategy.find_element('xpath=>//*[@id="heatMapdiv"]/div[1]/div[2]/div/button[5]').click()  # 点击南华商品
        time.sleep(3)
        # 策略指数
        strategy.find_element('xpath=>//*[@id="strategyIndexdiv"]/button[1]').click()  # 点击私募全市场
        time.sleep(3)
        strategy.find_element('xpath=>//*[@id="strategyIndexdiv"]/button[12]').click()  # 组合策略指数
        time.sleep(2)
        # 统计区间
        strategy.find_element('xpath=>//*[@id="y2"]').click()  # 2Y
        time.sleep(5)
