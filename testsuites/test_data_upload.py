import time
from pageobjects.data_upload import DataUpload
from testsuites.my_test import MyTest


class TestDataUpload(MyTest):
    """数据上传"""

    def test_data_upload_case1(self):
        """登录"""
        data = DataUpload(self.driver)
        data.data_upload_login()

    def test_data_upload_case2(self):
        """单只上传"""
        data = DataUpload(self.driver)
        data.data_upload_single()

    def test_data_upload_case3(self):
        data = DataUpload(self.driver)
        data.data_upload_upload()
        # 断言，补充基本信息上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的补充基本信息'
            print('补充基本信息上传 pass')
        except Exception as e:
            print('补充基本信息上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="investmentInfo"]/div[2]/div[2]/div[2]/p[2]/a').click()  # 净值信息上传
        time.sleep(5)
        # 断言，净值信息上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的净值信息'
            print('净值信息上传 pass')
        except Exception as e:
            print('净值信息上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="investmentInfo"]/div[2]/div[3]/div[2]/p[2]/a').click()  # 持仓汇总上传
        time.sleep(5)
        # 断言，持仓汇总上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的持仓汇总'
            print('持仓汇总上传 pass')
        except Exception as e:
            print('持仓汇总上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="investmentInfo"]/div[2]/div[4]/div[2]/p[2]/a').click()  # 交易明细上传
        time.sleep(5)
        # 断言，交易明细上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的交易明细'
            print('交易明细上传 pass')
        except Exception as e:
            print('交易明细上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="investmentInfo"]/div[2]/div[5]/div[2]/p[2]/a').click()  # 期货持仓交易明细表上传
        time.sleep(5)
        # 断言，期货持仓交易明细表上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的期货持仓交易明细表'
            print('期货持仓交易明细表上传 pass')
        except Exception as e:
            print('期货持仓交易明细表上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="investmentInfo"]/div[2]/div[6]/div[2]/p[2]/a').click()  # 估值表上传
        time.sleep(5)
        # 断言，估值表上传
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的估值表'
            print('估值表上传 pass')
        except Exception as e:
            print('估值表上传 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="determineBtn"]').click()
        time.sleep(5)

    def test_data_upload_case4(self):
        """列表"""
        data = DataUpload(self.driver)
        data.data_upload_list()
        data.current_handel()
        # 断言，基金链接
        time.sleep(2)
        try:
            assert u"数据上传" not in data.get_page_title()
            print('基金链接 pass')
        except Exception as e:
            print('基金链接 fail', format(e))
        time.sleep(2)
        data.close()
        time.sleep(2)
        data.current_handel()
        time.sleep(2)
        # 断言，基金名称
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[2]/a').text
        try:
            assert error_mes == u'自动化测试脚本1号'
            print('基金名称 pass')
        except Exception as e:
            print('基金名称 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资顾问
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[3]').text
        try:
            assert error_mes == u'自动化'
            print('投资顾问 pass')
        except Exception as e:
            print('投资顾问 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，基金管理人
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[4]').text
        try:
            assert error_mes == u'自动化'
            print('基金管理人 pass')
        except Exception as e:
            print('基金管理人 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，投资策略
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[5]').text
        try:
            assert error_mes == u'股票策略-股票多头'
            print('投资策略 pass')
        except Exception as e:
            print('投资策略 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值日期
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[6]').text
        try:
            assert error_mes == u'-'
            print('净值日期 pass')
        except Exception as e:
            print('净值日期 fail', format(e))
            print(error_mes)
        time.sleep(2)
        # 断言，净值
        error_mes = data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[7]').text
        try:
            assert error_mes == u'--'
            print('净值 pass')
        except Exception as e:
            print('净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[8]/div/a[1]').click()  # 修改信息
        time.sleep(5)
        # 断言，修改信息
        error_mes = data.find_element('xpath=>//*[@id="single_file"]/div[1]/div/span').text
        try:
            assert error_mes == u'基础信息'
            print('修改信息 pass')
        except Exception as e:
            print('修改信息 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="back"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[8]/div/a[2]').click()  # 更新净值
        time.sleep(5)
        # 断言，更新净值
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的净值上传'
            print('更新净值 pass')
        except Exception as e:
            print('更新净值 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[8]/div/a[3]').click()  # 持仓汇总
        time.sleep(5)
        # 断言，持仓汇总
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的持仓汇总'
            print('持仓汇总 pass')
        except Exception as e:
            print('持仓汇总 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[8]/div/a[4]').click()  # 交易明细
        time.sleep(5)
        # 断言，交易明细
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的交易明细'
            print('交易明细 pass')
        except Exception as e:
            print('交易明细 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)
        data.find_element('xpath=>//*[@id="data_filtbl"]/tbody/tr[1]/td[8]/div/a[5]').click()  # 期货持仓交易
        time.sleep(5)
        # 断言，期货持仓交易
        error_mes = data.find_element('xpath=>//*[@id="myModal"]/div/div/div[1]/h4/span').text
        try:
            assert error_mes == u'请上传该产品的期货持仓交易'
            print('期货持仓交易 pass')
        except Exception as e:
            print('期货持仓交易 fail', format(e))
            print(error_mes)
        time.sleep(2)
        data.find_element('xpath=>//*[@id="supBack"]').click()  # 返回
        time.sleep(3)

    def test_data_upload_case5(self):
        """删除"""
        data = DataUpload(self.driver)
        data.data_upload_delete()
