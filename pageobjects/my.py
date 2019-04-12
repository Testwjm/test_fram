import time
from framework.base_page import BasePage


class PowerMy(BasePage):
    """我的"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    my_click = 'xpath=>//*[@id="navUl"]/li[2]/a/span'  # 我的
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    strategy = 'xpath=>//*[@id="fundModule"]/div[1]/span[8]'  # 多策略
    my_public = 'xpath=>//*[@id="historyUl"]/li[2]'  # 公募

    def power_my_login(self):
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)

    def power_my_click(self):
        self.click(self.my_click)
