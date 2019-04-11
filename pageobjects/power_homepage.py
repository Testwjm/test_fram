from framework.base_page import BasePage
import time


class PowerHomePage(BasePage):
    """首页"""
    public_data = 'xpath=>/html/body/section/div[3]/div[1]/div[1]/span[2]'  # 公募数据
    public_text = '//*[@id="num2"]/div/div[1]/span[2]'
    private_data = 'xpath=>/html/body/section/div[3]/div[1]/div[1]/span[1]'  # 私募数据
    index_sm = 'xpath=>//*[text()="私募全市场指数"]'  # 私募全市场指数
    index_nfi = 'xpath=>//*[text()="南华商品指数"]'  # 南华商品指数
    drop_down = 'xpath=>//*[@id="dropDown"]/img'  # 展开
    drop_up = 'xpath=>//*[@id="dropUp"]/img'  # 收起
    welcome_join = 'xpath=>/html/body/section/div[5]/button'  # 欢迎加入
    confirm = 'xpath=>//*[@id="join"]/div/div/div[3]/button'  # 确定
    hyper_link = 'xpath=>/html/body/section/div[6]/div[2]/div[1]/a/div[1]'  # 第一个超链接

    def power_homepage_public(self):
        self.click(self.public_data)  # 点击公募数据

    def power_homepage_private(self):
        self.click(self.private_data)  # 点击私募数据

    def power_homepage_index(self):
        self.click(self.index_sm)  # 点击私募全市场指数
        time.sleep(2)
        self.click(self.index_nfi)  # 点击南华商品指数

    def power_homepage_dropdown(self):
        self.click(self.drop_down)  # 展开

    def power_homepage_welcome(self):
        self.click(self.drop_up)  # 收起
        self.click(self.welcome_join)  # 欢迎加入

    def power_homepage_link(self):
        self.click(self.confirm)  # 确定
        time.sleep(3)
        self.click(self.hyper_link)  # 点击超链接
