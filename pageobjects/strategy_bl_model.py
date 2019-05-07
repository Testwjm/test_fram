import time
from framework.base_page import BasePage


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
    next_step = 'xpath=>//*[@id="nextBtn1"]'  # 下一步

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
        pass
