import time
from framework.base_page import BasePage


class PrivateManager(BasePage):
    """私募基金经理详情页"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    fund_manager = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[3]/a'  # 基金经理
    key_word = 'xpath=>//*[@id="keyword"]'  # 关键字
    sure = 'xpath=>//*[@id="pubconfirmBtn"]'  # 确定
    details = 'xpath=>//*[@id="main-grid"]/tbody/tr[1]/td[2]/a'  # 基金经理链接
    y1_manager = 'xpath=>//*[@id="lastYear"]'  # 近一年
    y1_rank = 'xpath=>//*[@id="indexanalysis"]/button[3]'  # 近一年
    y1_risk = 'xpath=>//*[@id="rankingDate2"]/button[2]'  # 近一年
    super_yield = 'xpath=>//*[@id="profit"]/option[2]'  # 超额年化收益率
    bate_coefficient = 'xpath=>//*[@id="change"]/option[4]'  # 贝塔系数
    up_list = 'xpath=>//*[@id="incomeUl"]/li[2]'  # 已清盘基金
    fund_link = 'xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[1]/a'  # 基金链接
    mechanism_link = 'xpath=>//*[@id="institutions"]/span'  # 所在机构链接

    def private_manager_login(self):
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
        self.click(self.fund_manager)
        time.sleep(5)

    def private_manager_details(self):
        """头部"""
        self.type(self.key_word, '赵军')
        time.sleep(3)
        self.click(self.sure)
        time.sleep(8)
        self.click(self.details)
        time.sleep(5)

    def private_manager_profit(self):
        """累计收益率"""
        self.click(self.y1_manager)
        time.sleep(5)

    def private_manager_rank(self):
        """同类排名"""
        self.click(self.y1_rank)
        time.sleep(5)

    def private_manager_risk(self):
        """收益风险比"""
        self.click(self.y1_risk)
        time.sleep(8)
        self.click(self.super_yield)
        time.sleep(8)
        self.click(self.bate_coefficient)
        time.sleep(8)

    def private_manager_list(self):
        """产品列表"""
        self.click(self.up_list)
        time.sleep(5)
        self.click(self.fund_link)
        time.sleep(5)

    def private_manager_info(self):
        """基本信息"""
        self.click(self.mechanism_link)
        time.sleep(5)

