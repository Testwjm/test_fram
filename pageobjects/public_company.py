import time
from framework.base_page import BasePage


class PublicCompany(BasePage):
    """公募公司详情页"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    attend_excavate = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[2]/a'  # 投顾挖掘
    public_company = 'xpath=>//*[@id="choiceTbl"]/div[1]/ul/li[2]'  # 公募公司
    key_word = 'xpath=>//*[@id="keywordSearchpub"]'  # 关键字
    sure = 'xpath=>//*[@id="maindetermineBtnpub"]'  # 确定
    company_link = 'xpath=>//*[@id="main-grid-pub"]/tbody/tr/td[2]/a'  # 公司链接
    fund_link = 'xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[2]/a'  # 基金链接
    fund_manager = 'xpath=>//*[@id="fundManageTab"]/li[2]/span'  # 基金经理
    manager_link = 'xpath=>//*[@id="fundgManageModule"]/div[1]/div[2]/span/a'  # 基金经理链接

    def public_company_login(self):
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
        self.click(self.attend_excavate)
        time.sleep(5)
        self.click(self.public_company)
        time.sleep(5)

    def public_company_details(self):
        """头部"""
        self.type(self.key_word, '华夏基金管理有限公司')
        time.sleep(2)
        self.click(self.sure)
        time.sleep(5)
        self.click(self.company_link)
        time.sleep(5)

    def public_company_fund(self):
        """基金"""
        self.click(self.fund_link)
        time.sleep(5)

    def public_company_manager(self):
        """基金经理"""
        self.click(self.fund_manager)
        time.sleep(5)
        self.click(self.manager_link)
        time.sleep(5)

