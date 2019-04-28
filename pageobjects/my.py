import time
from framework.base_page import BasePage


class My(BasePage):
    """我的"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    my_click = 'xpath=>//*[@id="navUl"]/li[2]/a/span'  # 我的
    strategy = 'xpath=>//*[@id="fundModule"]/div[1]/span[8]'  # 多策略
    export_data = 'xpath=>//*[@id="fundModule"]/div[2]/div[1]/div[1]/div[2]/div/button'  # 导出数据
    excel_data = 'xpath=>//*[@id="fundModule"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[6]'  # MS-Excel
    fund_link = 'xpath=>//*[@id="JR143296"]/td[3]/a'  # 基金简称链接
    public_offer = 'xpath=>//*[@id="historyUl"]/li[2]'  # 公募
    other_fund = 'xpath=>//*[@id="fundModule2"]/div[1]/span[6]'  # 公募-其他基金
    export_public_data = 'xpath=>//*[@id="fundModule2"]/div[2]/div[1]/div[1]/div[2]/div/button'  # 公募-导出数据
    excel_public_data = 'xpath=>//*[@id="fundModule2"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[6]'  # 公募-Ms-Excel
    fund_public_link = 'xpath=>//*[@id="000216"]/td[3]/a'  # 公募-基金简称链接
    attend_to = 'xpath=>//*[@id="historyUl"]/li[3]'  # 投顾
    attend_link = 'xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[3]/a'  # 投资顾问链接
    set_up = 'xpath=>//*[@id="setMenu"]/button[2]'  # 个人设置

    def my_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)
        self.click(self.my_click)
        time.sleep(2)

    def my_private(self):
        """我的收藏-私募"""
        self.click(self.strategy)
        time.sleep(5)
        self.click(self.export_data)
        time.sleep(2)
        self.click(self.excel_data)
        time.sleep(3)
        self.click(self.fund_link)
        time.sleep(5)

    def my_offer(self):
        """我的收藏-公募"""
        self.click(self.public_offer)
        time.sleep(5)
        self.click(self.other_fund)
        time.sleep(5)
        self.click(self.export_public_data)
        time.sleep(2)
        self.click(self.excel_public_data)
        time.sleep(3)
        self.click(self.fund_public_link)
        time.sleep(5)

    def my_attend(self):
        """我的收藏-投顾"""
        self.click(self.attend_to)
        time.sleep(5)
        self.click(self.attend_link)
        time.sleep(5)

    def my_setup(self):
        """个人设置"""
        self.click(self.set_up)
        time.sleep(5)
