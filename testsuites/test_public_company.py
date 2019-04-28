import time
from pageobjects.public_company import PublicCompany
from testsuites.MyTest import MyTest


class TestPublicCompany(MyTest):
    """公募公司详情页"""

    def test_public_company_case1(self):
        """登录"""
        public = PublicCompany(self.driver)
        public.public_company_login()

    def test_public_company_case2(self):
        """头部"""
        public = PublicCompany(self.driver)
        public.public_company_details()
        public.current_handel()
        time.sleep(2)
        # 断言，公募公司详情
        try:
            assert u"华夏基金管理有限公司" in public.get_page_title()
            print('公募公司详情 pass')
        except Exception as e:
            print('公募公司详情 fail', format(e))
        time.sleep(2)
        '''头部'''
        # 断言，公募投顾基金公司名称
        error_mes = public.find_element('xpath=>//*[@id="investmentCompany"]').text
        try:
            assert error_mes == u'华夏基金管理有限公司'
            print('公募投顾基金公司名称 pass')
        except Exception as e:
            print('公募投顾基金公司名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾管理规模
        error_mes = public.find_element('xpath=>//*[@id="netScale"]').text
        try:
            assert error_mes != u'--'
            print('公募投顾管理规模 pass')
        except Exception as e:
            print('公募投顾管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾成立日期
        error_mes = public.find_element('xpath=>//*[@id="foundationDate"]').text
        try:
            assert error_mes == u'1998-04-09'
            print('公募投顾成立日期 pass')
        except Exception as e:
            print('公募投顾成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾办公地址
        error_mes = public.find_element('xpath=>//*[@id="orgAddress"]').text
        try:
            assert error_mes == u'北京市西城区金融大街33号通泰大厦B座8层'
            print('公募投顾办公地址 pass')
        except Exception as e:
            print('公募投顾办公地址 fail', format(e))
            print(error_mes)
        time.sleep(2)
        public.find_element('xpath=>//*[@id="net"]').click()
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        # 断言，公司网址地址链接
        try:
            assert u"华夏基金管理有限公司" not in public.get_page_title()
            print('公司网址地址链接 pass')
        except Exception as e:
            print('公司网址地址链接 fail', format(e))
        time.sleep(2)
        public.close()
        time.sleep(2)
        public.current_handel()
        time.sleep(2)

    def test_public_company_case3(self):
        """基金"""
        public = PublicCompany(self.driver)
        public.public_company_fund()
        public.current_handel()
        time.sleep(2)
        # 断言，基金链接
        try:
            assert u"华夏基金管理有限公司" not in public.get_page_title()
            print('基金链接 pass')
        except Exception as e:
            print('基金链接 fail', format(e))
        time.sleep(2)
        public.close()
        time.sleep(2)
        public.current_handel()
        time.sleep(2)
        # 断言，公募投顾基金代码
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[1]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金代码 pass')
        except Exception as e:
            print('公募投顾基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾基金名称
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[2]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金名称 pass')
        except Exception as e:
            print('公募投顾基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾基金类型
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金类型 pass')
        except Exception as e:
            print('公募投顾基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾基金经理
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金经理 pass')
        except Exception as e:
            print('公募投顾基金经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾最新净值
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes != u'--'
            print('公募投顾最新净值 pass')
        except Exception as e:
            print('公募投顾最新净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾最新规模（亿元)
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('公募投顾最新规模 pass')
        except Exception as e:
            print('公募投顾最新规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾成立日期
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('公募投顾成立日期 pass')
        except Exception as e:
            print('公募投顾成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾成立以来收益率
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes != u'--'
            print('公募投顾成立以来收益率 pass')
        except Exception as e:
            print('公募投顾成立以来收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾同类排名
        error_mes = public.find_element('xpath=>//*[@id="stockTypeTable"]/tbody/tr[1]/td[9]').text
        try:
            assert error_mes != u'--'
            print('公募投顾同类排名 pass')
        except Exception as e:
            print('公募投顾同类排名 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_public_company_case4(self):
        """基金经理"""
        public = PublicCompany(self.driver)
        public.public_company_manager()
        public.current_handel()
        time.sleep(2)
        # 断言，基金经理链接
        try:
            assert u"公募基金经理详情页" in public.get_page_title()
            print('基金经理链接 pass')
        except Exception as e:
            print('基金经理链接 fail', format(e))
        time.sleep(2)
        public.close()
        time.sleep(2)
        public.current_handel()
        time.sleep(2)
        public.find_element('xpath=>//*[@id="tab0"]/tbody/tr[1]/td[2]/a').click()  # 点击基金名称
        time.sleep(5)
        public.current_handel()
        time.sleep(2)
        # 断言，基金链接
        try:
            assert u"华夏基金管理有限公司" not in public.get_page_title()
            print('基金链接 pass')
        except Exception as e:
            print('基金链接 fail', format(e))
        time.sleep(2)
        public.close()
        time.sleep(2)
        public.current_handel()
        time.sleep(2)
        # 断言，公募投顾基金代码
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[1]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金代码 pass')
        except Exception as e:
            print('公募投顾基金代码 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾基金名称
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[2]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金名称 pass')
        except Exception as e:
            print('公募投顾基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾基金类型
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[3]').text
        try:
            assert error_mes != u'--'
            print('公募投顾基金类型 pass')
        except Exception as e:
            print('公募投顾基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾最新净值
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[4]').text
        try:
            assert error_mes != u'--\n--'
            print('公募投顾最新净值 pass')
        except Exception as e:
            print('公募投顾最新净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾管理规模
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[5]').text
        try:
            assert error_mes != u'--\n--'
            print('公募投顾管理规模 pass')
        except Exception as e:
            print('公募投顾管理规模 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾任职起始日期
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[6]').text
        try:
            assert error_mes != u'--'
            print('公募投顾任职起始日期 pass')
        except Exception as e:
            print('公募投顾任职起始日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾任职终止日期
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[7]').text
        try:
            assert error_mes == u'--'
            print('公募投顾任职终止日期 pass')
        except Exception as e:
            print('公募投顾任职终止日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，公募投顾任职期间收益率
        error_mes = public.find_element('xpath=>//*[@id="tab0"]/tbody/tr/td[8]').text
        try:
            assert error_mes != u'--'
            print('公募投顾任职期间收益率 pass')
        except Exception as e:
            print(format(e), '公募投顾任职期间收益率 fail')
            print(error_mes)
        time.sleep(2)
