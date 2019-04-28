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
        pass

    def product_management_details(self):
        """头部"""
        pass

    def product_management_history(self):
        """历史净值"""
        pass

    def product_management_rank(self):
        """同类排名"""
        pass

    def product_management_month_index(self):
        """月频指标"""
        pass

    def product_management_week_index(self):
        """周频指标"""
        pass

    def product_management_info(self):
        """基本信息"""
        pass

    def product_management_position(self):
        """持仓分析"""
        pass

    def product_management_account(self):
        """持仓分析-资产账户"""
        pass

    def product_management_shares(self):
        """持仓分析-股票资产"""
        pass

    def product_management_futures(self):
        """持仓分析-期货资产"""
        pass

    def product_management_bond(self):
        """持仓分析-债券资产"""
        pass

    def product_management_attribution(self):
        """净值归因"""
        pass

    def product_management_attribution_account(self):
        """持仓归因-资产账户"""
        pass

    def product_management_attribution_shares(self):
        """持仓归因-股票资产"""
        pass

    def product_management_attribution_futures(self):
        """持仓归因-期货资产"""
        pass

    def product_management_scene(self):
        """情景分析"""
        pass
