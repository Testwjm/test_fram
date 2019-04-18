import time
from framework.base_page import BasePage


class PrivateCompany(BasePage):
    """私募公司详情页"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screen = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    attend_excavate = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[2]/a/span'  # 投顾挖掘
    keyword = 'xpath=>//*[@id="keywordSearch"]'  # 关键字
    determine = 'xpath=>//*[@id="maindetermineBtn"]'  # 确定
    link = 'xpath=>//*[@id="main-grid"]/tbody/tr/td[3]/a'  # 上海高毅资产链接
    company_url = 'xpath=>//*[@id="netNav"]'  # 公司网址
    core_personnel = 'xpath=>//*[@id="org_name"]/a[1]'  # 核心人员卓利伟
    show_all = 'xpath=>//*[@id="org_return_btn"]/button[2]'  # 显示全部
    y1_rank = 'xpath=>//*[@id="rankingDate"]/button[3]'  # 近一年同类排名
    record_information = 'xpath=>//*[@id="menuUl"]/li[2]/a'  # 备案信息
    performance_indicators = 'xpath=>//*[@id="menuUl"]/li[3]/a'  # 业绩指标
    its_products = 'xpath=>//*[@id="menuUl"]/li[4]/a'  # 旗下产品
    macro_strategy = 'xpath=>//*[@id="6010601"]'  # 宏观策略
    team_information = 'xpath=>//*[@id="menuUl"]/li[5]/a'  # 团队信息
    fund_manager = 'xpath=>//*[@id="teamTab"]/tbody/tr[1]/td[2]/a'  # 基金经理

    def private_company_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)

    def private_company_details(self):
        """进入详情页"""
        self.click(self.pre_screen)
        time.sleep(1)
        self.click(self.attend_excavate)
        time.sleep(3)
        self.type(self.keyword, '上海高毅资产')
        time.sleep(1)
        self.click(self.determine)
        time.sleep(3)
        self.click(self.link)
        time.sleep(5)

    def private_company_url(self):
        """头部，公司网址"""
        self.click(self.company_url)
        time.sleep(5)

    def private_company_personnel(self):
        """核心人员"""
        self.click(self.core_personnel)
        time.sleep(5)

    def private_company_trend(self):
        """投顾综合指数走势"""
        self.click(self.show_all)
        time.sleep(5)

    def private_company_rank(self):
        """同类排名"""
        self.click(self.y1_rank)
        time.sleep(5)

    def private_record_information(self):
        """备案信息"""
        self.click(self.record_information)
        time.sleep(5)

    def private_performance_indicators(self):
        """业绩指标"""
        self.click(self.performance_indicators)
        time.sleep(5)

    def private_its_products(self):
        """旗下产品"""
        self.click(self.its_products)
        time.sleep(15)
        self.click(self.macro_strategy)
        time.sleep(5)

    def private_team_information(self):
        """团队信息"""
        self.click(self.team_information)
        time.sleep(8)
        self.click(self.fund_manager)
        time.sleep(5)
