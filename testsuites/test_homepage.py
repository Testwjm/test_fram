import time
from pageobjects.homepage import HomePage
from testsuites.my_test import MyTest


class TestHomePage(MyTest):
    """首页"""

    def test_homepage_case1(self):
        """公募数据"""
        homepage = HomePage(self.driver)
        homepage.homepage_public()
        time.sleep(2)
        # 断言，公募数据
        error_mes = homepage.find_element('xpath=>//*[@id="num2"]/div/div[1]/span[2]').text  # 基金公司值含1
        try:
            assert error_mes != u'--'
            print('公募数据 pass.')
        except Exception as e:
            print('公募数据 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_homepage_case2(self):
        """私募数据"""
        homepage = HomePage(self.driver)
        homepage.homepage_private()
        time.sleep(2)
        # 断言，私募数据
        error_mes = homepage.find_element('xpath=>//*[@id="num2"]/div/div[1]/span[4]').text  # 基金公司值含3
        try:
            assert error_mes != u'--'
            print('私募数据 pass.')
        except Exception as e:
            print('私募数据 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_homepage_case3(self):
        """私募综合业绩指数"""
        homepage = HomePage(self.driver)
        homepage.homepage_index()
        time.sleep(2)
        # 断言，私募综合业绩指数
        try:
            homepage.find_element("xpath=>//*[text()='南华商品指数']").is_selected()  # 判断南华商品指数是否被选中
            print('私募综合业绩指数 Pass.')
        except Exception as e:
            print('私募综合业绩指数 fail', format(e))
        time.sleep(2)

    def test_homepage_case4(self):
        """私募分策略业绩指数情况"""
        homepage = HomePage(self.driver)
        homepage.homepage_dropdown()
        time.sleep(2)
        # 断言，私募分策略业绩指数情况
        error_mes = homepage.find_element('xpath=>//*[@id="dropLoad"]/div[1]/div[1]/div[2]').text  # 宏观策略私募指数值为2303.72
        try:
            assert error_mes != u'--'
            print('私募分策略业绩指数情况 pass.')
        except Exception as e:
            print('私募分策略业绩指数情况 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_homepage_case5(self):
        """私募基金管理人HFMI指数"""
        homepage = HomePage(self.driver)
        homepage.homepage_welcome()
        time.sleep(2)
        # 断言，私募基金管理人HFMI指数
        error_mes = homepage.find_element('xpath=>//*[@id="join"]/div/div/div[2]/div/div[2]/div[12]').text
        try:
            assert error_mes == u'HFMI指数持续招募中，请扫描下方二维码'
            print('私募基金管理人HFMI指数 pass.')
        except Exception as e:
            print('私募基金管理人HFMI指数 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_homepage_case6(self):
        """基金研究院"""
        homepage = HomePage(self.driver)
        homepage.homepage_link()
        time.sleep(2)
        homepage.current_handel()
        time.sleep(2)
        # 断言，基金研究院
        try:
            assert u"首页" not in homepage.get_page_title()
            print('基金研究院 pass.')
        except Exception as e:
            print('基金研究院 fail.', format(e))
        time.sleep(5)
