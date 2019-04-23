import time
from framework.base_page import BasePage


class PublicManager(BasePage):
    """公募基金经理详情页"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    fund_manager = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[3]/a'  # 基金经理
    public_manager = 'xpath=>//*[@id="addNewprcdiv"]/div[1]/ul/li[2]'  # 公募基金经理
    key_word = 'xpath=>//*[@id="keywordSearch"]'  # 关键字
    public_sure = 'xpath=>//*[@id="maindetermineBtn"]'  # 确定
    public_details = 'xpath=>//*[@id="main-grid2"]/tbody/tr/td[2]/a'  # 基金经理链接
    public_y1 = 'xpath=>//*[@id="lastYear"]'  # 近一年
    rank_y1 = 'xpath=>//*[@id="indexanalysis"]/button[3]'  # 近一年
    risk_y1 = 'xpath=>//*[@id="rankingDate2"]/button[2]'  # 近一年
    excess_profit = 'xpath=>//*[@id="profit"]/option[2]'  # 超额年化收益率
    bate_coefficient = 'xpath=>//*[@id="change"]/option[4]'  # 贝塔系数
    history_fund = 'xpath=>//*[@id="incomeUl"]/li[2]'  # 历史管理基金
    fund_link = 'xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[2]/span'  # 基金名称链接

    def public_manager_login(self):
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
        time.sleep(8)

    def public_manager_details(self):
        """公募基金详情页"""
        self.click(self.public_manager)
        time.sleep(2)
        self.type(self.key_word, '陈凯杨')
        time.sleep(2)
        self.click(self.public_sure)
        time.sleep(8)
        self.click(self.public_details)
        time.sleep(5)

    def public_manager_head(self):
        """头部"""
        self.click(self.public_y1)
        time.sleep(5)

    def public_manager_ranking(self):
        """同类排名"""
        self.click(self.rank_y1)
        time.sleep(5)

    def public_manager_risk(self):
        """收益风险比"""
        self.click(self.risk_y1)
        time.sleep(5)
        self.click(self.excess_profit)
        time.sleep(5)
        self.click(self.bate_coefficient)
        time.sleep(5)

    def public_manager_list(self):
        """产品列表"""
        self.click(self.history_fund)
        time.sleep(5)
        self.click(self.fund_link)
        time.sleep(5)

    def public_manager_info(self):
        """基本信息"""
        pass
