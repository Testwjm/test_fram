import time
from framework.base_page import BasePage
import random


class StrategyMvModel(BasePage):
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
    next_step = 'xpath=>//*[@id="nextBtn1"]'  # 下一步
    bind_return = 'xpath=>//*[@id="return_a"]'  # 年化收益率
    bind_wave = 'xpath=>//*[@id="std_a"]'  # 年化波动率
    bind_risk = 'xpath=>//*[@id="risk_free"]'  # 无风险收益率
    bind_subfundmin = 'xpath=>//*[@id="subfundMin"]'  # 子基金权重下限
    bind_subfundmax = 'xpath=>//*[@id="subfundMax"]'  # 子基金权重上限
    target_next_step = 'xpath=>//*[@id="nextBtn2"]'  # 下一步
    sure = 'xpath=>//*[@id="createCompolicy"]/div/div/div[8]/div[3]/button[2]'  # 确定

    # def date_name(self):
    #     from datetime import datetime
    #     from random import randint
    #     n = randint(100, 99)
    #     s = str(datetime.now().date()) + "-" + str(n)
    #     return s

    def strategy_mv_login(self):
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

    def strategy_mv_establish(self):
        """创建新的策略组合"""
        self.type(self.strategy_name, 'MV模型-')
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
        self.click(self.next_step)
        time.sleep(5)

    def strategy_mv_target(self):
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

    def strategy_mv_compose(self):
        """策略组合"""
        self.click(self.sure)
        time.sleep(15)
