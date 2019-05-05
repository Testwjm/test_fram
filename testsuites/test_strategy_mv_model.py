import time
from pageobjects.strategy_mv_model import StrategyMvModel
from testsuites.my_test import MyTest


class TestStrategyMvModel(MyTest):
    """策略组合-MV模型"""

    def test_strategy_mv_case1(self):
        """登录"""
        strategy = StrategyMvModel(self.driver)
        strategy.strategy_mv_login()

    def test_strategy_mv_case2(self):
        """创建新的策略组合"""
        strategy = StrategyMvModel(self.driver)
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
        strategy.strategy_mv_establish()

    def test_strategy_mv_case3(self):
        strategy = StrategyMvModel(self.driver)
        # 断言，目标设定
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[2]/div[2]/div[2]/span').text
        try:
            assert error_mes == u'目标设定'
            print('目标设定 pass')
        except Exception as e:
            print('目标设定 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，目标函数选择
        error_mes = strategy.find_element(
            'xpath=>//*[@id="targetSet"]/div[1]/span').text
        try:
            assert error_mes == u'目标函数选择'
            print('目标函数选择 pass')
        except Exception as e:
            print('目标函数选择 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，选择约束条件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="conditionSet"]/div[1]/span').text
        try:
            assert error_mes == u'选择约束条件'
            print('选择约束条件 pass')
        except Exception as e:
            print('选择约束条件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指数名称
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step2Tbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'私募全市场指数'
            print('指数名称 pass')
        except Exception as e:
            print('指数名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step2Tbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('区间年化收益率 pass')
        except Exception as e:
            print('区间年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step2Tbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('区间最大回撤 pass')
        except Exception as e:
            print('区间最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step2Tbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('区间年化夏普比 pass')
        except Exception as e:
            print('区间年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，区间年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step2Tbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('区间年化波动率 pass')
        except Exception as e:
            print('区间年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.strategy_mv_target()

    def test_strategy_mv_case4(self):
        strategy = StrategyMvModel(self.driver)
        # 断言，Benchmark
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step3showInfo"]/tbody/tr/td[1]/div[2]').text
        try:
            assert error_mes == u'沪深300,南华商品指数'
            print('Benchmark pass')
        except Exception as e:
            print('Benchmark fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置模式
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step3showInfo"]/tbody/tr/td[2]/div[2]').text
        try:
            assert error_mes == u'MV模型'
            print('配置模式 pass')
        except Exception as e:
            print('配置模式 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，内外样本区间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step3showInfo"]/tbody/tr/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('内外样本区间 pass')
        except Exception as e:
            print('内外样本区间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，目标既定
        error_mes = strategy.find_element(
            'xpath=>//*[@id="step3showInfo"]/tbody/tr/td[4]/div[2]').text
        try:
            assert error_mes == u'年化夏普比最大'
            print('目标既定 pass')
        except Exception as e:
            print('目标既定 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，全样本区间约束条件
        error_mes = strategy.find_element(
            'xpath=>').text
        try:
            assert error_mes == u'--'
            print('全样本区间约束条件 pass')
        except Exception as e:
            print('全样本区间约束条件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，全样本区间约束条件
        error_mes = strategy.find_element(
            'xpath=>//*[@id="Conditions"]').text
        try:
            assert error_mes == u'年化收益率>=2%,年化波动<=3%,无风险收益率5% .'
            print('全样本区间约束条件 pass')
        except Exception as e:
            print('全样本区间约束条件 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，指数名称
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'私募全市场指数'
            print('指数名称 pass')
        except Exception as e:
            print('指数名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes == u'--'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes == u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，配置比例
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes == u'--'
            print('配置比例 pass')
        except Exception as e:
            print('配置比例 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，拟投资金额（万元
        error_mes = strategy.find_element(
            'xpath=>//*[@id="creatPrctbl"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes == u'--'
            print('拟投资金额（万元) pass')
        except Exception as e:
            print('拟投资金额（万元) fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，有效边界
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[8]/div[2]/div[4]/div[1]/div[1]/div/span').text
        try:
            assert error_mes == u'有效边界'
            print('有效边界 pass')
        except Exception as e:
            print('有效边界 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，组合预期业绩指标
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/div/div/span').text
        try:
            assert error_mes == u'组合预期业绩指标'
            print('组合预期业绩指标 pass')
        except Exception as e:
            print('组合预期业绩指标 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[1]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[1]/td[2]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[1]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化下行标准差
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[2]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化下行标准差 pass')
        except Exception as e:
            print('年化下行标准差 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，Sortino比率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[2]/td[2]/div[2]').text
        try:
            assert error_mes == u'--'
            print('Sortino比率 pass')
        except Exception as e:
            print('Sortino比率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[2]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[3]/td[1]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤发生时间
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[3]/td[2]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤发生时间 pass')
        except Exception as e:
            print('最大回撤发生时间 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤形成期
        error_mes = strategy.find_element(
            'xpath=>//*[@id="mvTbldiv"]/table/tbody/tr[3]/td[3]/div[2]').text
        try:
            assert error_mes != u'--'
            print('最大回撤形成期 pass')
        except Exception as e:
            print('最大回撤形成期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[8]/div[2]/div[5]/div/div[1]/div/span').text
        try:
            assert error_mes == u'累计收益率'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，期间收益率
        error_mes = strategy.find_element(
            'xpath=>//*[@id="createCompolicy"]/div/div/div[8]/div[2]/div[6]/div/div[1]/div/span').text
        try:
            assert error_mes == u'期间收益率'
            print('期间收益率 pass')
        except Exception as e:
            print('期间收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        strategy.execute_script_down()
        time.sleep(2)
        strategy.strategy_mv_compose()

    def test_strategy_mv_case5(self):
        pass

    def test_strategy_mv_case6(self):
        pass
