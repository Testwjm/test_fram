import time
from framework.base_page import BasePage


class IndustryData(BasePage):
    """行业数据"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    industry_data = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[4]/a'  # 行业数据
    product_quantity = 'xpath=>//*[@id="assetUl"]/li[2]'  # 基金产品数量
    management_scale = 'xpath=>//*[@id="assetUl"]/li[3]'  # 管理基金规模
    data_clear = 'xpath=>//*[@id="mainemptyBtn"]'  # 清空
    nfi_data = 'xpath=>//*[@id="nfi"]'  # 南华期货指数
    fi13_data = 'xpath=>//*[@id="FI13"]'  # 组合投资策略指数
    month_data = 'xpath=>//*[@id="y"]'  # 月频
    sure_data = 'xpath=>//*[@id="maindetermineBtn"]'  # 确定
    fi131_data = 'xpath=>//*[@id="strategyIndexdiv"]/button[12]'  # 组合策略指数
    index_center = 'xpath=>//*[@id="labUl"]/li[2]/span'  # 指数中心

    def industry_data_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)
        self.click(self.pre_screening)
        time.sleep(2)
        self.click(self.industry_data)
        time.sleep(5)

    def industry_data_situation(self):
        """私募登记备案情况"""
        self.click(self.product_quantity)
        time.sleep(5)

    def industry_data_drogue(self):
        """指数涨跌风向标"""
        pass

    def industry_data_trend(self):
        """策略指数走势"""
        self.click(self.data_clear)
        time.sleep(2)
        self.click(self.nfi_data)
        time.sleep(2)
        self.click(self.fi13_data)
        time.sleep(2)
        self.click(self.month_data)
        time.sleep(2)
        self.click(self.sure_data)
        time.sleep(5)

    def industry_data_relativity(self):
        """指数相关性"""
        self.click(self.fi131_data)
        time.sleep(3)

    def industry_data_list(self):
        """指数列表"""
        self.click(self.index_center)
        time.sleep(5)

