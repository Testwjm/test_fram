import time
from framework.base_page import BasePage


class PrivateFund(BasePage):
    """私募基金详情页"""

    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    product_perspective = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[1]/a'  # 产品透视
    key_word = 'xpath=>//*[@id="keywordSearch"]'  # 关键字输入框
    sure = 'xpath=>//*[@id="maindetermineBtn"]'  # 确定
    detail = 'xpath=>//*[@id="JR000001"]/td[3]/a'  # 详情页链接
    show_all = 'xpath=>//*[@id="showAll"]'  # 显示全部
    export_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/button'  # 导出数据
    csv_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[1]'  # CSV
    excel_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[2]'  # ms-excel
    y1_rank = 'xpath=>//*[@id="rankingDate"]/button[3]'  # 近一年
    week_index = 'xpath=>//*[@id="freqDiv"]/div[1]'  # 周频指标
    nv_attribution = 'xpath=>//*[@id="menuImg3"]'  # 净值归因
    ff_model = 'xpath=>//*[@id="tabs"]/ul/li[2]'  # FF模型
    barra_model = 'xpath=>//*[@id="tabs"]/ul/li[3]'  # barra模型
    scene_analysis = 'xpath=>//*[@id="menuUl"]/li[4]'  # 情景分析
    futures_market = 'xpath=>//*[@id="incomeUl"]/li[3]'  # 管理期货市场

    def private_fund_login(self):
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
        self.click(self.product_perspective)
        time.sleep(5)

    def private_fund_detail(self):
        """头部"""
        self.type(self.key_word, 'JR000001')
        time.sleep(3)
        self.click(self.sure)
        time.sleep(5)
        self.click(self.detail)
        time.sleep(5)

    def private_fund_history(self):
        """历史净值"""
        self.click(self.show_all)
        time.sleep(5)
        self.click(self.export_data)
        time.sleep(2)
        self.click(self.csv_data)
        time.sleep(2)
        self.click(self.export_data)
        time.sleep(2)
        self.click(self.excel_data)
        time.sleep(2)

    def private_fund_rank(self):
        """同类排名"""
        self.click(self.y1_rank)
        time.sleep(5)

    def private_fund_month_index(self):
        """月频指标"""
        pass

    def private_fund_week_index(self):
        """周频指标"""
        self.click(self.week_index)
        time.sleep(5)

    def private_fund_nv(self):
        """净值归因"""
        self.click(self.nv_attribution)
        time.sleep(5)

    def private_fund_ff(self):
        """FF模型"""
        self.click(self.nv_attribution)
        time.sleep(5)
        self.click(self.ff_model)
        time.sleep(5)

    def private_fund_barra(self):
        """barra模型"""
        self.click(self.nv_attribution)
        time.sleep(5)
        self.click(self.barra_model)
        time.sleep(5)

    def private_fund_scene(self):
        """情景分析"""
        self.click(self.scene_analysis)
        time.sleep(8)
        self.click(self.futures_market)
        time.sleep(5)
