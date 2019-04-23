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

    def private_manager_login(self):
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
