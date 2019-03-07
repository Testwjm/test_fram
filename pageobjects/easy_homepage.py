from framework.base_page import BasePage


class FofPowerHomepage(BasePage):
    """登录"""
    search_my = 'xpath=>//*[@id="navUl"]/li[2]/a/span'  # 点击我的
    input_userName = 'xpath=>//*[@id="userName"]'  # 输入手机号码
    input_password = 'xpath=>//*[@id="password"]'  # 输入密码
    search_submit_dl = 'id=>btnSubmit'  # 点击登录

    def type_power_search(self):
        self.click(self.search_my)  # 点击我的

    def input_power_username(self, text):
        self.type(self.input_userName, text)  # 输入手机号码

    def input_power_password(self, text):
        self.type(self.input_password, text)  # 输入密码

    def search_power_submit(self):
        self.click(self.search_submit_dl)  # 点击登录
