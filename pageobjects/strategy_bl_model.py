import time
from framework.base_page import BasePage
import random


class StrategyBlModel(BasePage):
    """策略组合-BL模型"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    asset_allocation = 'xpath=>//*[@id="navUl"]/li[4]/span'  # 资产配置
    strategy_combination = 'xpath=>//*[@id="navUl"]/li[4]/ul/li[1]/a/span'  # 策略组合
    add_strategy = 'xpath=>//*[@id="addNewcomply"]'  # 添加新的策略组合
    strategy_name = 'xpath=>//*[@id="newPrcname"]'  # 新建策略名称
    investment_amount = 'xpath=>//*[@id="investmentAmountinp"]'  # 投资金额
    benchmark_hs300 = 'xpath=>//*[@id="createCompolicy"]/div/div/div[1]/div[2]/div[4]/div[2]/div[1]/label'  # 沪深300
    benchmark_nfi = 'xpath=>//*[@id="createCompolicy"]/div/div/div[1]/div[2]/div[4]/div[2]/div[5]/label'  # 南华商品指数
    strategy_nfi = 'xpath=>//*[@id="industrymainTbl"]/tbody/tr[1]/td[2]/button[5]'  # 南华期货指数
    strategy_fio3 = 'xpath=>//*[@id="industrymainTbl"]/tbody/tr[2]/td[2]/button[2]'  # 私募fof指数
    strategy_fi13 = 'xpath=>//*[@id="industrymainTbl"]/tbody/tr[2]/td[2]/button[12]'  # 组合投资策略指数
    within_section = 'xpath=>//*[@id="createCompolicy"]/div/div/div[1]/div[2]/div[6]/div[2]/div[2]/label'  # 内样本区间
    bl_model = 'xpath=>//*[@id="ConfigModel"]/div[2]/div[2]/label'  # BL模型
    next_step = 'xpath=>//*[@id="nextBtn1"]'  # 下一步
    bind_return = 'xpath=>//*[@id="yq_return_a"]'  # 预期年化收益率
    bind_wave = 'xpath=>//*[@id="yq_std_a"]'  # 预期年化波动率
    bind_risk = 'xpath=>//*[@id="yq_risk_free"]'  # 预期无风险收益率
    bind_subfundmin = 'xpath=>//*[@id="yqSubfundMin"]'  # 预期子基金权重下限
    bind_subfundmax = 'xpath=>//*[@id="yqSubfundMax"]'  # 预期子基金权重上限
    target_next_step = 'xpath=>//*[@id="nextBL"]'  # 下一步
    sure = 'xpath=>//*[@id="createCompolicy"]/div/div/div[5]/div[3]/button[2]'  # 确定
    nv_y1 = 'xpath=>//*[@id="lastYear"]'  # 近一年
    nv_download = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/button'  # 下载
    nv_csv = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[1]'  # CSV
    nv_excel = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[2]'  # Excel
    position_analysis = 'xpath=>//*[@id="menuUl"]/li[2]'  # 持仓分析
    nv_attribution = 'xpath=>//*[@id="menuUl"]/li[3]'  # 净值归因
    scenario_analysis = 'xpath=>//*[@id="menuUl"]/li[4]'  # 情景分析
    delete = 'xpath=>//*[@id="policyCom"]/ul/li[1]/div[1]/span[1]/button'  # 删除
    delete_sure = 'xpath=>//*[@id="layui-layer1"]/div[3]/a[1]'  # 确认删除

    def strategy_bl_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)
        self.click(self.asset_allocation)
        time.sleep(2)
        self.click(self.strategy_combination)
        time.sleep(5)
        self.click(self.add_strategy)
        time.sleep(5)

    def strategy_bl_establish(self):
        """创建新的策略组合"""
        self.type(self.strategy_name, 'BL模型-' + str(random.randrange(1000, 10000)))
        time.sleep(2)
        self.type(self.investment_amount, '1000')
        time.sleep(2)
        self.click(self.benchmark_hs300)
        time.sleep(2)
        self.click(self.benchmark_nfi)
        time.sleep(2)
        self.click(self.strategy_nfi)
        time.sleep(2)
        self.click(self.strategy_fio3)
        time.sleep(2)
        self.click(self.strategy_fi13)
        time.sleep(2)
        self.click(self.within_section)
        time.sleep(2)
        self.click(self.bl_model)
        time.sleep(3)
        self.click(self.next_step)
        time.sleep(5)

    def strategy_bl_target(self):
        """目标设定"""
        self.type(self.bind_return, '2')
        time.sleep(2)
        self.type(self.bind_wave, '3')
        time.sleep(2)
        self.type(self.bind_risk, '5')
        time.sleep(2)
        self.clear(self.bind_subfundmin)
        time.sleep(2)
        self.type(self.bind_subfundmin, '10')
        time.sleep(2)
        self.clear(self.bind_subfundmax)
        time.sleep(2)
        self.type(self.bind_subfundmax, '40')
        time.sleep(2)
        self.click(self.target_next_step)
        time.sleep(10)

    def strategy_bl_compose(self):
        """策略组合"""
        self.click(self.sure)
        time.sleep(15)

    def strategy_bl_head(self):
        """头部"""
        pass

    def strategy_bl_history(self):
        """历史净值"""
        self.click(self.nv_y1)
        time.sleep(5)
        self.click(self.nv_download)
        time.sleep(2)
        self.click(self.nv_csv)
        time.sleep(3)
        self.click(self.nv_download)
        time.sleep(2)
        self.click(self.nv_excel)
        time.sleep(3)

    def strategy_bl_index(self):
        """指标"""
        pass

    def strategy_bl_position(self):
        """持仓分析"""
        self.click(self.position_analysis)
        time.sleep(5)

    def strategy_bl_attribution(self):
        """净值归因"""
        self.click(self.nv_attribution)
        time.sleep(5)

    def strategy_bl_scene(self):
        """情景分析"""
        self.click(self.scenario_analysis)
        time.sleep(5)

    def strategy_bl_delete(self):
        """删除"""
        self.click(self.asset_allocation)
        time.sleep(3)
        self.click(self.strategy_combination)
        time.sleep(5)
        self.click(self.delete)
        time.sleep(3)
        self.click(self.delete_sure)
        time.sleep(5)

    def strategy_bl_exponent(self):
        """指数"""
        pass
