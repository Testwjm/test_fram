import time
from framework.base_page import BasePage


class PublicFund(BasePage):
    """公募基金详情页"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    pre_screening = 'xpath=>//*[@id="navUl"]/li[3]/span'  # 投前筛选
    product_perspective = 'xpath=>//*[@id="navUl"]/li[3]/ul/li[1]/a'  # 产品透视
    public_fund = 'xpath=>//*[@id="choiceTbl"]/div[1]/ul/li[2]'  # 公募基金
    key_word = 'xpath=>//*[@id="keywords"]'  # 关键字
    sure = 'xpath=>//*[@id="pubconfirmBtn"]'  # 确定
    fund_name = 'xpath=>//*[@id="000001"]/td[4]/a'  # 详情页
    show_all = 'xpath=>//*[@id="showAll"]'  # 显示全部
    export_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/button'  # 导出数据
    csv_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[1]'  # CSV
    excel_data = 'xpath=>//*[@id="netTbl"]/div[1]/div[1]/div/div/ul/li[2]'  # Excel
    y1_rank = 'xpath=>//*[@id="rankingDate"]/button[3]'  # 近一年
    basic_info = 'xpath=>//*[@id="menuUl"]/li[1]'  # 基本信息
    position_analysis = 'xpath=>//*[@id="menuUl"]/li[3]'  # 持仓分析
    nv_attribution = 'xpath=>//*[@id="menuImg3"]'  # 净值归因
    ff_model = 'xpath=>//*[@id="tabs"]/ul/li[2]'  # FF模型
    position_attribution = 'xpath=>//*[@id="positionAttr"]'  # 持仓归因
    scene_analysis = 'xpath=>//*[@id="menuUl"]/li[6]'  # 情景分析

    def public_fund_login(self):
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
        self.click(self.public_fund)
        time.sleep(5)

    def public_fund_details(self):
        """头部"""
        self.type(self.key_word, '000001')
        time.sleep(2)
        self.click(self.sure)
        time.sleep(5)
        self.click(self.fund_name)
        time.sleep(5)

    def public_fund_history(self):
        """历史净值"""
        self.click(self.show_all)
        time.sleep(5)
        self.click(self.export_data)
        time.sleep(2)
        self.click(self.csv_data)
        time.sleep(3)
        self.click(self.export_data)
        time.sleep(2)
        self.click(self.excel_data)
        time.sleep(3)

    def public_fund_rank(self):
        """同类排名"""
        self.click(self.y1_rank)
        time.sleep(5)

    def public_fund_index(self):
        """指标"""
        pass

    def public_fund_info(self):
        """基本信息"""
        self.click(self.basic_info)
        time.sleep(5)

    def public_fund_positions(self):
        """持仓分析"""
        self.click(self.position_analysis)
        time.sleep(2)

    def public_fund_sharp(self):
        """夏普模型"""
        self.click(self.nv_attribution)
        time.sleep(8)

    def public_fund_ff(self):
        """FF模型"""
        self.click(self.nv_attribution)
        time.sleep(8)
        self.click(self.ff_model)
        time.sleep(5)

    def public_fund_barra(self):
        """持仓归因"""
        self.click(self.position_attribution)
        time.sleep(25)

    def public_fund_scene(self):
        """情景分析"""
        self.click(self.scene_analysis)
        time.sleep(8)

