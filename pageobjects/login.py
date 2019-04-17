import time
from framework.base_page import BasePage


class Login(BasePage):
    """登录"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录

    def login_homepage(self):
        self.click(self.homepage)

    def login_username(self, text):
        self.type(self.username, text)

    def login_password(self, text):
        self.type(self.password, text)

    def login_button(self):
        self.click(self.button)

    def login_clear(self):
        self.clear(self.username)
        time.sleep(2)
        self.clear(self.password)
