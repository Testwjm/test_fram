import time
from framework.base_page import BasePage


class ProductManagement(BasePage):
    """产品管理"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    throw_manage = 'xpath=>//*[@id="navUl"]/li[5]/span'  # 投后管理
    product_management = 'xpath=>//*[@id="navUl"]/li[5]/ul/li[1]/a/span'  # 产品管理
    add_product = 'xpath=>//*[@id="toSelfLoaded"]/span[2]'  # 添加产品
    fund_link = 'xpath=>//*[@id="listFuntTab"]/tbody/tr[1]/td[1]/a'  # 基金链接
    show_all = 'xpath=>//*[@id="showAll"]'  # 显示全部
    m3_rank = 'xpath=>//*[@id="similarRankingsSLT"]/option[2]'  # 近三个月
    week_index = 'xpath=>//*[@id="freqDiv"]/div[1]'  # 周频
    base_info = 'xpath=>//*[@id="menuUl"]/li[1]/a'  # 基本信息
    position_analysis = 'xpath=>//*[@id="menuUl"]/li[3]'  # 持仓分析
    stock_assets = 'xpath=>//*[@id="positionUl"]/li[2]'  # 股票资产
    futures_assets = 'xpath=>//*[@id="positionUl"]/li[3]'  # 期货资产
    bond_assets = 'xpath=>//*[@id="positionUl"]/li[4]'  # 债券资产
    nv_attribution = 'xpath=>//*[@id="menuUl"]/li[4]/a'  # 净值归因
    position_attribution = 'xpath=>//*[@id="menuUl"]/li[5]'  # 持仓归因
    position_stock_assets = 'xpath=>//*[@id="assetUl"]/li[2]'  # 持仓归因-股票资产
    position_futures_assets = 'xpath=>//*[@id="assetUl"]/li[3]'  # 持仓归因-期货资产
    scenario_analysis = 'xpath=>//*[@id="menuUl"]/li[6]'  # 情景分析

    def product_management_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(5)
        self.click(self.throw_manage)
        time.sleep(2)
        self.click(self.product_management)
        time.sleep(5)

    def product_management_list(self):
        """列表"""
        self.click(self.add_product)
        time.sleep(5)

    def product_management_details(self):
        """头部"""
        self.click(self.fund_link)
        time.sleep(5)

    def product_management_history(self):
        """历史净值"""
        self.click(self.show_all)
        time.sleep(5)

    def product_management_rank(self):
        """同类排名"""
        self.click(self.m3_rank)
        time.sleep(5)

    def product_management_month_index(self):
        """月频指标"""
        pass

    def product_management_week_index(self):
        """周频指标"""
        self.click(self.week_index)
        time.sleep(5)

    def product_management_info(self):
        """基本信息"""
        self.click(self.base_info)
        time.sleep(5)

    def product_management_position(self):
        """持仓分析"""
        self.click(self.position_analysis)
        time.sleep(5)

    def product_management_account(self):
        """持仓分析-资产账户"""
        pass

    def product_management_shares(self):
        """持仓分析-股票资产"""
        self.click(self.stock_assets)
        time.sleep(15)

    def product_management_futures(self):
        """持仓分析-期货资产"""
        self.click(self.futures_assets)
        time.sleep(15)

    def product_management_bond(self):
        """持仓分析-债券资产"""
        self.click(self.bond_assets)
        time.sleep(15)

    def product_management_attribution(self):
        """净值归因"""
        self.click(self.nv_attribution)
        time.sleep(5)

    def product_management_attribution_account(self):
        """持仓归因-资产账户"""
        self.click(self.position_attribution)
        time.sleep(25)

    def product_management_attribution_shares(self):
        """持仓归因-股票资产"""
        self.click(self.position_stock_assets)
        time.sleep(15)

    def product_management_attribution_futures(self):
        """持仓归因-期货资产"""
        self.click(self.position_futures_assets)
        time.sleep(10)

    def product_management_scene(self):
        """情景分析"""
        self.click(self.scenario_analysis)
        time.sleep(10)

