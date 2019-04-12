from selenium import webdriver
from time import sleep


class Login:
    def __init__(self, **kwargs):
        self.kw = kwargs
        self.password = self.kw.get("password")
        self.username = self.kw.get("username")

    def init_user(self):
        if self.password is None or self.username is None:
            self.username = "15107045860"
            self.password = "045860"

    def login(self, driver):
        """登录"""
        self.init_user()
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://power.fofpower.com")  # 生产环境
        # driver.get("http://innertest.fofpower.com/")  # 测试环境
        driver.implicitly_wait(10)
        sleep(3)
        driver.maximize_window()
        sleep(3)
        # 我的
        driver.find_element_by_xpath('//*[@id="navUl"]/li[2]/a/span').click()  # 点击我的
        driver.implicitly_wait(10)
        sleep(2)
        # 登录
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(self.username)  # 输入手机号码
        sleep(2)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)  # 输入密码
        sleep(2)
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()  # 点击登录
        driver.implicitly_wait(10)
        sleep(5)
        return driver
