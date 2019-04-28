import time
from pageobjects.private_manager import PrivateManager
from testsuites.my_test import MyTest


class TestPrivateManager(MyTest):
    """私募基金经理详情页"""

    def test_private_manager_case1(self):
        """登录"""
        private = PrivateManager(self.driver)
        private.private_manager_login()

    def test_private_manager_case2(self):
        """头部"""
        private = PrivateManager(self.driver)
        private.private_manager_details()
        private.current_handel()
        time.sleep(2)
        # 断言，详情页
        try:
            assert u"私募基金经理详情页" in private.get_page_title()
            print('私募基金经理详情 pass')
        except Exception as e:
            print('私募基金详情 fail', format(e))
        time.sleep(2)
        '''头部'''
        # 断言，基金公司
        error_mes = private.find_element('xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes == u'北京淡水泉投资'
            print('基金公司 pass')
        except Exception as e:
            print('基金公司 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，从业年限
        error_mes = private.find_element('xpath=>//*[@id="wyear"]').text
        try:
            assert error_mes != u'--'
            print('从业年限 pass')
        except Exception as e:
            print('从业年限 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计管理数量
        error_mes = private.find_element('xpath=>//*[@id="number"]').text
        try:
            assert error_mes != u'--'
            print('累计管理数量 pass')
        except Exception as e:
            print('累计管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，在任管理数量
        error_mes = private.find_element('xpath=>//*[@id="scale"]').text
        try:
            assert error_mes != u'--'
            print('在任管理数量 pass')
        except Exception as e:
            print('在任管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，履历背景
        error_mes = private.find_element('xpath=>//*[@id="working"]').text
        try:
            assert error_mes == u'公募'
            print('履历背景 pass')
        except Exception as e:
            print('履历背景 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，擅长策略
        error_mes = private.find_element('xpath=>//*[@id="strategy"]').text
        try:
            assert error_mes == u'股票多空'
            print('擅长策略 pass')
        except Exception as e:
            print('擅长策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，代表产品
        error_mes = private.find_element('xpath=>//*[@id="produce"]/a').text
        try:
            assert error_mes == u'平安信托-淡水泉2008'
            print('代表产品 pass')
        except Exception as e:
            print('代表产品 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_manager_case3(self):
        """累计收益率"""
        private = PrivateManager(self.driver)
        private.private_manager_profit()
        # 断言，累计收益率
        error_mes = private.find_element('xpath=>/html/body/section/div[2]/div[1]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'累计收益率'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，产品分布
        error_mes = private.find_element('xpath=>/html/body/section/div[2]/div[2]/div[1]/div/span').text
        try:
            assert error_mes == u'产品分布'
            print('产品分布 pass')
        except Exception as e:
            print('产品分布 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_manager_case4(self):
        """同类排名"""
        private = PrivateManager(self.driver)
        private.private_manager_rank()
        error_mes1 = private.find_element(
            'xpath=>//*[@id="rankingText"]').text
        error_mes = error_mes1.split('，')[0]  # # 获取这句话逗号前的语句
        try:
            assert error_mes == u'中期综合评价中'
            print('中期综合评价 pass')
        except Exception as e:
            print('中期综合评价 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = private.find_element('xpath=>//*[@id="rankingText"]/i[1]').text  # 获取近一年语句的排名
        one = one.replace('(', '').replace(')', '')  # 处理获取的值，去掉括号
        time.sleep(2)
        tow = private.find_element('xpath=>//*[@id="y1"]').text  # 获取近一年图表的排名
        try:  # 对比两者是否相同
            assert one == tow
            print('近一年排名一致 pass')
        except Exception as e:
            print('近一年排名不一致 fail', format(e))
        time.sleep(2)

    def test_private_manager_case5(self):
        """收益风险比"""
        private = PrivateManager(self.driver)
        private.private_manager_risk()
        # 断言，收益风险比
        error_mes = private.find_element('xpath=>/html/body/section/div[4]/div[3]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'收益风险比'
            print('收益风险比 pass')
        except Exception as e:
            print('收益风险比 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_manager_case6(self):
        """产品列表"""
        private = PrivateManager(self.driver)
        # 断言，运行中基金名称
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[1]/a').text
        try:
            assert error_mes != u'--'
            print('运行中基金名称 pass')
        except Exception as e:
            print('运行中基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金投资策略
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('运行中基金投资策略 pass')
        except Exception as e:
            print('运行中基金投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金任职日期
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('运行中基金任职日期 pass.')
        except Exception as e:
            print('运行中基金任职日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金最新净值日期
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('运行中基金最新净值日期 pass')
        except Exception as e:
            print('运行中基金最新净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金单位净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('运行中基金单位净值 pass')
        except Exception as e:
            print('运行中基金单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金累计净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('运行中基金累计净值 pass')
        except Exception as e:
            print('运行中基金累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金复权累计净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('运行中基金复权累计净值 pass')
        except Exception as e:
            print('运行中基金复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，运行中基金任职以来收益率
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes != u'--'
            print('运行中基金任职以来收益率 pass')
        except Exception as e:
            print('运行中基金任职以来收益率值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        private.private_manager_list()
        private.current_handel()
        time.sleep(2)
        # 断言，详情页
        try:
            assert u"私募基金经理详情页" not in private.get_page_title()
            print('私募基金经理详情 pass')
        except Exception as e:
            print('私募基金详情 fail', format(e))
        time.sleep(2)
        private.close()
        time.sleep(2)
        private.current_handel()
        time.sleep(2)
        # 断言，已清盘基金名称
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[1]/a').text
        try:
            assert error_mes != u'--'
            print('已清盘基金名称 pass')
        except Exception as e:
            print('已清盘基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金投资策略
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金投资策略 pass')
        except Exception as e:
            print('已清盘基金投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金任职日期
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金任职日期 pass')
        except Exception as e:
            print('已清盘基金任职日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金最新净值日期
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金最新净值日期 pass')
        except Exception as e:
            print('已清盘基金最新净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金单位净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金单位净值 pass')
        except Exception as e:
            print('已清盘基金单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金累计净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金累计净值 pass')
        except Exception as e:
            print('已清盘基金累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金复权累计净值
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金复权累计净值 pass')
        except Exception as e:
            print('已清盘基金复权累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，已清盘基金任职以来收益率
        error_mes = private.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes != u'--'
            print('已清盘基金任职以来收益率 pass')
        except Exception as e:
            print('已清盘基金任职以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_private_manager_case7(self):
        """基本信息"""
        private = PrivateManager(self.driver)
        private.private_manager_info()
        private.current_handel()
        time.sleep(2)
        # 断言，所在机构链接
        try:
            assert u"私募基金经理详情页" not in private.get_page_title()
            print('所在机构链接 pass')
        except Exception as e:
            print('所在机构链接 fail', format(e))
        time.sleep(2)
        private.close()
        time.sleep(2)
        private.current_handel()
        time.sleep(2)
        # 断言，基金经理姓名
        error_mes = private.find_element('xpath=>//*[@id="tname"]').text
        try:
            assert error_mes == u'赵军'
            print('基金经理姓名 pass')
        except Exception as e:
            print('基金经理姓名 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，从业年限
        error_mes = private.find_element('xpath=>//*[@id="tdate"]').text
        try:
            assert error_mes != u'--'
            print('从业年限 pass')
        except Exception as e:
            print('从业年限 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，性别
        error_mes = private.find_element('xpath=>//*[@id="tsex"]').text
        try:
            assert error_mes != u'--'
            print('性别 pass')
        except Exception as e:
            print('性别 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，是否具备基金从业资格
        error_mes = private.find_element('xpath=>//*[@id="tedu"]').text
        try:
            assert error_mes == u'是'
            print('是否具备基金从业资格 pass.')
        except Exception as e:
            print('是否具备基金从业资格 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，履历背景
        error_mes = private.find_element('xpath=>//*[@id="teducation"]').text
        try:
            assert error_mes == u'公募'
            print('履历背景 pass.')
        except Exception as e:
            print('履历背景 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，学历
        error_mes = private.find_element('xpath=>//*[@id="workexperience"]').text
        try:
            assert error_mes == u'硕士'
            print('学历 pass')
        except Exception as e:
            print('学历 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，毕业院校
        error_mes = private.find_element('xpath=>//*[@id="tyear"]').text
        try:
            assert error_mes == u'南开大学'
            print('毕业院校 pass')
        except Exception as e:
            print('毕业院校 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，所在机构
        error_mes = private.find_element('xpath=>//*[@id="institutions"]').text
        try:
            assert error_mes == u'北京淡水泉投资'
            print('所在机构 pass')
        except Exception as e:
            print('所在机构 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，任职公司数量
        error_mes = private.find_element('xpath=>//*[@id="cnumber"]').text
        try:
            assert error_mes != u'--'
            print('任职公司数量 pass')
        except Exception as e:
            print('任职公司数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计管理数量
        error_mes = private.find_element('xpath=>//*[@id="pnumber"]').text
        try:
            assert error_mes != u'--'
            print('累计管理数量 pass')
        except Exception as e:
            print('累计管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，在任管理数量
        error_mes = private.find_element('xpath=>//*[@id="nnumber"]').text
        try:
            assert error_mes != u'--'
            print('在任管理数量 pass')
        except Exception as e:
            print('在任管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金经理简介
        error_mes = private.find_element('xpath=>//*[@id="introduction"]').text
        try:
            assert error_mes != u'--'
            print('基金经理简介 pass.')
        except Exception as e:
            print('基金经理简介 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''获奖基金'''
        # 断言，获奖年份
        error_mes = private.find_element('xpath=>//*[@id="award"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes == u'2010'
            print('获奖年份 pass')
        except Exception as e:
            print('获奖年份 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，奖项
        error_mes = private.find_element('xpath=>//*[@id="award"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes == u'第1届私募金牛奖'
            print('奖项 pass.')
        except Exception as e:
            print('奖项 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，具体奖项名称
        error_mes = private.find_element('xpath=>//*[@id="award"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes == u'金牛阳光私募投资经理'
            print('具体奖项名称 pass.')
        except Exception as e:
            print('具体奖项名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，颁奖机构
        error_mes = private.find_element('xpath=>//*[@id="award"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'中国证券报'
            print('颁奖机构 pass')
        except Exception as e:
            print('颁奖机构 fail', format(e))
            print(error_mes)
        time.sleep(5)