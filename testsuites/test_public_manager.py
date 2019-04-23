import time
from pageobjects.public_manager import PublicManager
from testsuites.MyTest import MyTest


class TestPublicManager(MyTest):
    """公募基金经理详情页"""

    def test_public_manager_case1(self):
        """登录"""
        public = PublicManager(self.driver)
        public.public_manager_login()

    def test_public_manager_case2(self):
        """基金经理详情页"""
        public = PublicManager(self.driver)
        public.public_manager_details()
        public.current_handel()
        time.sleep(2)
        # 断言，公募基金经理详情页
        try:
            assert u"公募基金经理详情页" in public.get_page_title()
            print('公募基金经理详情页 pass')
        except Exception as e:
            print('公募基金经理详情页 fail', format(e))
        time.sleep(2)

    def test_public_manager_case3(self):
        """头部"""
        public = PublicManager(self.driver)
        # 断言，基金公司
        error_mes = public.find_element('xpath=>//*[@id="Policy"]').text
        try:
            assert error_mes == u'博时基金'
            print('基金公司 pass')
        except Exception as e:
            print('基金公司 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金经理
        error_mes = public.find_element('xpath=>//*[@id="reg_code"]').text
        try:
            assert error_mes == u'基金经理'
            print('基金经理 pass')
        except Exception as e:
            print('基金经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，从业年限
        error_mes = public.find_element('xpath=>//*[@id="wyear"]').text
        try:
            assert error_mes != u'--'
            print('从业年限 pass')
        except Exception as e:
            print('从业年限 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计管理数量
        error_mes = public.find_element('xpath=>//*[@id="number"]').text
        try:
            assert error_mes != u'--'
            print('累计管理数量 pass')
        except Exception as e:
            print('累计管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，在任管理数量
        error_mes = public.find_element('xpath=>//*[@id="now_number"]').text
        try:
            assert error_mes != u'--'
            print('在任管理数量 pass')
        except Exception as e:
            print('在任管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，在任管理规模
        error_mes = public.find_element('xpath=>//*[@id="scale"]').text
        try:
            assert error_mes != u'--'
            print('在任管理规模 pass')
        except Exception as e:
            print('在任管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，擅长策略
        error_mes = public.find_element('xpath=>//*[@id="strategy"]').text
        try:
            assert error_mes == u'债券型'
            print('擅长策略 pass')
        except Exception as e:
            print('擅长策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，代表产品
        error_mes = public.find_element('xpath=>//*[@id="produce"]/a').text
        try:
            assert error_mes == u'博时双月薪定期支付债券'
            print('代表产品 pass')
        except Exception as e:
            print('代表产品 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = public.find_element('xpath=>/html/body/section/div[2]/div[1]/div[1]/div[1]/span').text
        try:
            assert error_mes == u'累计收益率'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.public_manager_head()
        # 断言，产品分布
        error_mes = public.find_element('xpath=>/html/body/section/div[2]/div[2]/div[1]/div/span').text
        try:
            assert error_mes == u'产品分布'
            print('产品分布 pass')
        except Exception as e:
            print('产品分布 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_manager_case4(self):
        """同类排名"""
        public = PublicManager(self.driver)
        public.public_manager_ranking()
        error_mes1 = public.find_element(
            'xpath=>//*[@id="rankingText"]').text
        error_mes = error_mes1.split('，')[0]  # 获取这句话逗号前的语句
        try:
            assert error_mes == u'中期综合评价中'
            print('中期综合评价 pass')
        except Exception as e:
            print('中期综合评价 fail', format(e))
            print(error_mes)
        time.sleep(2)
        one = public.find_element('xpath=>//*[@id="rankingText"]/i[1]').text  # 获取近一年语句的排名
        one = one.replace('(', '').replace(')', '')  # 处理获取的值，去掉括号
        time.sleep(2)
        tow = public.find_element('xpath=>//*[@id="y1"]').text  # 获取近一年图表的排名
        try:  # 对比两者是否相同
            assert one == tow
            print('近一年排名一致 pass')
        except Exception as e:
            print('近一年排名不一致 fail', format(e))
        time.sleep(2)

    def test_public_manager_case5(self):
        """收益风险比"""
        public = PublicManager(self.driver)
        # 断言，收益风险比
        error_mes = public.find_element('xpath=>/html/body/section/div[4]/div[3]/div[1]/div[2]/span').text
        try:
            assert error_mes == u'收益风险比'
            print('收益风险比 pass')
        except Exception as e:
            print('收益风险比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.public_manager_risk()

    def test_public_manager_case6(self):
        """产品列表"""
        public = PublicManager(self.driver)
        '''现任管理基金'''
        # 断言，非货币，现任基金代码
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('现任基金代码 pass')
        except Exception as e:
            print('现任基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任基金名称
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('现任基金名称 pass')
        except Exception as e:
            print('现任基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任基金类型
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('现任基金类型 pass')
        except Exception as e:
            print('现任基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任任职起始日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('现任任职起始日期 pass')
        except Exception as e:
            print('现任任职起始日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任最新单位净值
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--\n(--)'
            print('现任最新单位净值 pass')
        except Exception as e:
            print('现任最新单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任最新管理规模
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--\n(--)'
            print('非货币型现任最新管理规模 pass')
        except Exception as e:
            print('非货币型现任最新管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，现任任职期间收益率
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('现任任职期间收益率 pass')
        except Exception as e:
            print('现任任职期间收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任基金代码
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('现任基金代码 pass')
        except Exception as e:
            print('现任基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任基金名称
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('现任基金名称 pass')
        except Exception as e:
            print('现任基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任基金类型
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes == u'货币型'
            print('现任基金类型 pass')
        except Exception as e:
            print('现任基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任任职起始日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('现任任职起始日期 pass')
        except Exception as e:
            print('现任任职起始日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任最新万份收益
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--\n(--)'
            print('现任最新万份收益 pass')
        except Exception as e:
            print('现任最新万份收益 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任最新7日年化
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--\n(--)'
            print('现任最新7日年化 pass')
        except Exception as e:
            print('现任最新7日年化 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，现任最新管理规模
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--\n(--)'
            print('货币型现任最新管理规模 pass')
        except Exception as e:
            print('货币型现任最新管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.public_manager_list()
        public.current_handel()
        time.sleep(2)
        # 断言，基金详情页
        try:
            assert u"公募基金经理详情页" not in public.get_page_title()
            print('基金详情页 pass')
        except Exception as e:
            print('基金详情页 fail', format(e))
        time.sleep(2)
        public.close()
        public.current_handel()
        time.sleep(2)
        # 断言，非货币，历史基金代码
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('非货币型历史基金代码 pass')
        except Exception as e:
            print('非货币型历史基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史基金名称
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('非货币型历史基金名称 pass')
        except Exception as e:
            print('非货币型历史基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史基金类型
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('非货币型历史基金类型 pass')
        except Exception as e:
            print('非货币型历史基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史任职起始日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('非货币型历史任职起始日期 pass')
        except Exception as e:
            print('非货币型历史任职起始日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史任职终止日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('非货币型历史任职终止日期 pass')
        except Exception as e:
            print('非货币型历史任职终止日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史管理规模
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--\n(--)'
            print('非货币型历史管理规模 pass')
        except Exception as e:
            print('非货币型历史管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，非货币，历史任职期间收益率
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('历史任职期间收益率 pass')
        except Exception as e:
            print('历史任职期间收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史基金代码
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('货币型历史基金代码 pass.')
        except Exception as e:
            print('货币型历史基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史基金名称
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('货币型历史基金名称 pass')
        except Exception as e:
            print('货币型历史基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史基金类型
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes == u'货币型'
            print('货币型历史基金类型 pass')
        except Exception as e:
            print('货币型历史基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史任职起始日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('货币型历史任职起始日期 pass.')
        except Exception as e:
            print('货币型历史任职起始日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史任职终止日期
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('货币型历史任职终止日期 pass')
        except Exception as e:
            print('货币型历史任职终止日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史管理规模
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--\n(--)'
            print('货币型历史管理规模 pass')
        except Exception as e:
            print('货币型历史管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，货币，历史7日年化收益平均值
        error_mes = public.find_element('xpath=>//*[@id="rateindicatorsCharts2"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('历史7日年化收益平均值 pass')
        except Exception as e:
            print('历史7日年化收益平均值 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_manager_case7(self):
        """基本信息"""
        public = PublicManager(self.driver)
        public.public_manager_info()
        # 断言，基金经理姓名
        error_mes = public.find_element('xpath=>//*[@id="tname"]').text
        try:
            assert error_mes == u'陈凯杨'
            print('基金经理姓名 pass.')
        except Exception as e:
            print('基金经理姓名 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，从业年限
        error_mes = public.find_element('xpath=>//*[@id="tyear"]').text
        try:
            assert error_mes != u'--'
            print('从业年限 pass.')
        except Exception as e:
            print('从业年限 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，性别
        error_mes = public.find_element('xpath=>//*[@id="tsex"]').text
        try:
            assert error_mes != u'--'
            print('性别 pass')
        except Exception as e:
            print('性别 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，学历
        error_mes = public.find_element('xpath=>//*[@id="tedu"]').text
        try:
            assert error_mes != u'--'
            print('学历 pass')
        except Exception as e:
            print('学历 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金经理简介
        error_mes = public.find_element('xpath=>//*[@id="introduction"]').text
        try:
            assert error_mes != u'--'
            print('基金经理简介 pass')
        except Exception as e:
            print('基金经理简介 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，任职公司数量
        error_mes = public.find_element('xpath=>//*[@id="cnumber"]').text
        try:
            assert error_mes != u'--'
            print('任职公司数量 pass')
        except Exception as e:
            print('任职公司数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计管理数量
        error_mes = public.find_element('xpath=>//*[@id="pnumber"]').text
        try:
            assert error_mes != u'--'
            print('累计管理数量 pass')
        except Exception as e:
            print('累计管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，在任管理数量
        error_mes = public.find_element('xpath=>//*[@id="nnumber"]').text
        try:
            assert error_mes != u'--'
            print('在任管理数量 pass')
        except Exception as e:
            print('在任管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''从业经历'''
        # 断言，任职以来
        error_mes = public.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr/td[1]').text
        try:
            assert error_mes != u'--'
            print('任职以来 pass')
        except Exception as e:
            print('任职以来 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，任职公司
        error_mes = public.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr/td[2]').text
        try:
            assert error_mes == u'博时基金'
            print('任职公司 pass')
        except Exception as e:
            print('任职公司 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计管理数量
        error_mes = public.find_element('xpath=>//*[@id="similarRankingsTab"]/tbody/tr/td[3]').text
        try:
            assert error_mes != u'--'
            print('累计管理数量 pass')
        except Exception as e:
            print('累计管理数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        '''获奖基金'''
        # 断言，基金简称
        error_mes = public.find_element('xpath=>//*[@id="award"]/tbody/tr/td[1]').text
        try:
            assert error_mes == u'博时双月薪'
            print('基金简称 pass.')
        except Exception as e:
            print('基金简称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，获奖年份
        error_mes = public.find_element('xpath=>//*[@id="award"]/tbody/tr/td[2]').text
        try:
            assert error_mes == u'2016'
            print('获奖年份 pass')
        except Exception as e:
            print('获奖年份 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，奖项
        error_mes = public.find_element('xpath=>//*[@id="award"]/tbody/tr/td[3]').text
        try:
            assert error_mes == u'三年持续回报普通债券型明星基金奖'
            print('奖项 pass')
        except Exception as e:
            print('奖项 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，颁奖机构
        error_mes = public.find_element('xpath=>//*[@id="award"]/tbody/tr/td[4]').text
        try:
            assert error_mes == u'证券时报'
            print('颁奖机构 pass')
        except Exception as e:
            print('颁奖机构 fail', format(e))
            print(error_mes)
        time.sleep(5)
