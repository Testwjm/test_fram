import time
from testsuites.MyTest import MyTest
from pageobjects.my import My


class TestMy(MyTest):
    """我的"""

    def test_my_case1(self):
        """登录"""
        my = My(self.driver)
        my.my_login()

    def test_my_case2(self):
        """我的收藏-私募"""
        my = My(self.driver)
        my.my_private()
        my.current_handel()
        time.sleep(2)
        # 断言，基金简称链接
        try:
            assert u"我的" not in my.get_page_title()
            print('基金简称链接 pass')
        except Exception as e:
            print('基金简称链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        my.find_element('xpath=>//*[@id="JR143296"]/td[4]/a').click()  # 投资顾问链接
        time.sleep(5)
        my.current_handel()
        time.sleep(2)
        # 断言，投资顾问链接
        try:
            assert u"我的" not in my.get_page_title()
            print('投资顾问链接 pass')
        except Exception as e:
            print('投资顾问链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        my.find_element('xpath=>//*[@id="JR143296"]/td[5]/a').click()  # 基金经理链接
        time.sleep(5)
        my.current_handel()
        time.sleep(2)
        # 断言，投资经理链接
        try:
            assert u"我的" not in my.get_page_title()
            print('投资经理链接 pass')
        except Exception as e:
            print('投资经理链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        # 断言，基金简称
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[3]/a').text
        try:
            assert error_mes != u'--'
            print('基金简称 pass')
        except Exception as e:
            print('基金简称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资顾问
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[4]/a').text
        try:
            assert error_mes != u'--'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资经理
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[5]/a').text
        try:
            assert error_mes != u'--'
            print('投资经理 pass')
        except Exception as e:
            print('投资经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资策略
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[6]').text
        try:
            assert error_mes != u'--'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，发行主体
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[7]').text
        try:
            assert error_mes != u'--'
            print('发行主体 pass')
        except Exception as e:
            print('发行主体 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[8]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[9]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[10]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[11]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = my.find_element('xpath=>//*[@id="JR141668"]/td[12]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_my_case3(self):
        """我的收藏-公募"""
        my = My(self.driver)
        my.my_offer()
        my.current_handel()
        time.sleep(2)
        # 断言，基金简称链接
        try:
            assert u"我的" not in my.get_page_title()
            print('基金简称链接 pass')
        except Exception as e:
            print('基金简称链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        my.find_element('xpath=>//*[@id="000216"]/td[4]/a').click()  # 投资经理链接
        time.sleep(5)
        my.current_handel()
        time.sleep(2)
        # 断言，投资经理链接
        try:
            assert u"我的" not in my.get_page_title()
            print('投资经理链接 pass')
        except Exception as e:
            print('投资经理链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        # 断言，基金简称
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[3]/a').text
        try:
            assert error_mes != u'--'
            print('基金简称 pass')
        except Exception as e:
            print('基金简称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资经理
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[4]/a[1]').text
        try:
            assert error_mes != u'--'
            print('投资经理 pass')
        except Exception as e:
            print('投资经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[5]').text
        try:
            assert error_mes != u'--'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金类型
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[6]').text
        try:
            assert error_mes != u'--'
            print('基金类型 pass')
        except Exception as e:
            print('基金类型 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[7]').text
        try:
            assert error_mes != u'--'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，单位净值
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[8]').text
        try:
            assert error_mes != u'--'
            print('单位净值 pass')
        except Exception as e:
            print('单位净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计净值
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[9]').text
        try:
            assert error_mes != u'--'
            print('累计净值 pass')
        except Exception as e:
            print('累计净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[10]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = my.find_element('xpath=>//*[@id="000929"]/td[11]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_my_case4(self):
        """我的收藏-投顾"""
        my = My(self.driver)
        my.my_attend()
        my.current_handel()
        time.sleep(2)
        # 断言，投资顾问链接
        try:
            assert u"我的" not in my.get_page_title()
            print('投资顾问链接 pass')
        except Exception as e:
            print('投资顾问链接 fail', format(e))
        time.sleep(2)
        my.close()
        time.sleep(2)
        my.current_handel()
        time.sleep(2)
        # 断言，投资顾问
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[3]/a').text
        try:
            assert error_mes != u'--'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资经理
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[4]/span').text
        try:
            assert error_mes != u'--'
            print('投资经理 pass')
        except Exception as e:
            print('投资经理 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，主要策略
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[5]/span').text
        try:
            assert error_mes != u'--'
            print('主要策略 pass')
        except Exception as e:
            print('主要策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，成立日期
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes != u'--'
            print('成立日期 pass')
        except Exception as e:
            print('成立日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，存续产品数量
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes != u'--'
            print('存续产品数量 pass')
        except Exception as e:
            print('存续产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，管理产品数量
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[8]').text
        try:
            assert error_mes != u'--'
            print('管理产品数量 pass')
        except Exception as e:
            print('管理产品数量 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，累计收益率
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[9]').text
        try:
            assert error_mes != u'--'
            print('累计收益率 pass')
        except Exception as e:
            print('累计收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化收益率
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[10]').text
        try:
            assert error_mes != u'--'
            print('年化收益率 pass')
        except Exception as e:
            print('年化收益率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化夏普比
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[11]').text
        try:
            assert error_mes != u'--'
            print('年化夏普比 pass')
        except Exception as e:
            print('年化夏普比 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，年化波动率
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[12]').text
        try:
            assert error_mes != u'--'
            print('年化波动率 pass')
        except Exception as e:
            print('年化波动率 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，最大回撤
        error_mes = my.find_element('xpath=>//*[@id="castguTab"]/tbody/tr[1]/td[13]').text
        try:
            assert error_mes != u'--'
            print('最大回撤 pass')
        except Exception as e:
            print('最大回撤 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_my_case5(self):
        """个人设置"""
        my = My(self.driver)
        my.my_setup()
        # 断言，个人设置
        error_mes = my.find_element('xpath=>//*[@id="userInformation"]/div[1]/span').text
        try:
            assert error_mes == u'个人设置'
            print('个人设置 pass')
        except Exception as e:
            print('个人设置 fail', format(e))
            print(error_mes)
        time.sleep(5)
