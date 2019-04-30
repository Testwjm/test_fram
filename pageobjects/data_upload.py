import time
from framework.base_page import BasePage


class DataUpload(BasePage):
    """数据上传"""
    homepage = 'xpath=>//*[@id="navUl"]/li[1]/a'  # 首页
    username = 'xpath=>//*[@id="userName"]'  # 手机号
    password = 'xpath=>//*[@id="password"]'  # 密码
    button = 'xpath=>//*[@id="btnSubmit"]'  # 登录
    throw_manage = 'xpath=>//*[@id="navUl"]/li[5]/span'  # 投后管理
    data_upload = 'xpath=>//*[@id="navUl"]/li[5]/ul/li[2]/a/span'  # 数据上传
    down_load = 'xpath=>//*[@id="dataFildiv"]/div[1]/div/div[1]/a'  # 下载模板
    upload_explain = 'xpath=>//*[@id="dataFildiv"]/div[1]/div/div[2]/button[1]'  # 上传说明
    upload_close = 'xpath=>//*[@id="closeLayer"]'  # 关闭
    single_upload = 'xpath=>//*[@id="singUp"]'  # 单只上传
    product_name = 'xpath=>//*[@id="product_name"]'  # 产品名称
    found_date = 'xpath=>//*[@id="date_of_establishment"]'  # 成立日期
    today = 'xpath=>/html/body/div[9]/div[3]/table/tfoot/tr[1]/th'  # 今天
    investment_adviser = 'xpath=>//*[@id="investment_advisers"]'  # 投资顾问
    fund_manage = 'xpath=>//*[@id="fund_manager"]'  # 基金管理人
    invest_manage = 'xpath=>//*[@id="investment_manager"]'  # 投资经理
    template_one = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[1]/div[2]/p[1]/a'  # 补充基本信息下载
    template_two = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[2]/div[2]/p[1]/a'  # 净值信息下载
    template_three = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[3]/div[2]/p[1]/a'  # 持仓汇总下载
    template_four = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[4]/div[2]/p[1]/a'  # 交易明细下载
    template_five = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[5]/div[2]/p[1]/a'  # 期货持仓交易明细表下载
    template_six = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[6]/div[2]/p[1]/a'  # 估值表下载
    upload_one = 'xpath=>//*[@id="investmentInfo"]/div[2]/div[1]/div[2]/p[2]/a'  # 补充基本信息上传
    fund_link = 'xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[2]/a'  # 基金链接
    fund_delete = 'xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[9]'  # 删除
    delete = 'xpath=>//*[@id="layui-layer2"]/div[3]/a[1]'  # 确认删除

    def data_upload_login(self):
        """登录"""
        self.click(self.homepage)
        time.sleep(2)
        self.type(self.username, '15107045860')
        time.sleep(2)
        self.type(self.password, '045860')
        time.sleep(2)
        self.click(self.button)
        time.sleep(2)
        self.click(self.throw_manage)
        time.sleep(2)
        self.click(self.data_upload)
        time.sleep(5)

    def data_upload_single(self):
        """基础信息"""
        self.click(self.down_load)
        time.sleep(3)
        self.click(self.upload_explain)
        time.sleep(3)
        self.click(self.upload_close)
        time.sleep(3)
        self.click(self.single_upload)
        time.sleep(5)
        self.type(self.product_name, '自动化测试脚本1号')
        time.sleep(2)
        self.click(self.found_date)
        time.sleep(2)
        self.click(self.today)
        time.sleep(2)
        self.type(self.investment_adviser, '自动化')
        time.sleep(2)
        self.type(self.fund_manage, '自动化')
        time.sleep(2)
        self.type(self.invest_manage, '自动化')
        time.sleep(2)

    def data_upload_upload(self):
        """数据上传"""
        self.click(self.template_one)
        time.sleep(3)
        self.click(self.template_two)
        time.sleep(3)
        self.click(self.template_three)
        time.sleep(3)
        self.click(self.template_four)
        time.sleep(3)
        self.click(self.template_five)
        time.sleep(3)
        self.click(self.template_six)
        time.sleep(3)
        self.click(self.upload_one)
        time.sleep(5)

    def data_upload_list(self):
        """列表"""
        self.click(self.fund_link)
        time.sleep(5)

    def data_upload_delete(self):
        """删除"""
        self.click(self.fund_delete)
        time.sleep(5)
        self.click(self.delete)
        time.sleep(5)
