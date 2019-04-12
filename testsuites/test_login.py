import time
from pageobjects.login import PowerLogin
from testsuites.MyTest import MyTest


class FofPowerLogin(MyTest):
    """登录"""

    def test_login_a(self):
        """手机号、密码为空"""
        login = PowerLogin(self.driver)
        login.power_login_homepage()
        time.sleep(2)
        login.power_login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="userName"]').text
        try:
            assert error_mes == u''
            print('手机号、密码为空 pass.')
        except Exception as e:
            print('手机号、密码为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_b(self):
        """密码为空，手机号不为空"""
        login = PowerLogin(self.driver)
        login.power_login_username('15107045860')
        time.sleep(2)
        login.power_login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="password"]').text
        try:
            assert error_mes == u''
            print('密码为空，手机号不为空 pass.')
        except Exception as e:
            print('密码为空，手机号不为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_c(self):
        """手机号为空，密码不为空"""
        login = PowerLogin(self.driver)
        login.power_login_clear()
        time.sleep(2)
        login.power_login_password('045860')
        time.sleep(2)
        login.power_login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="userName"]').text
        try:
            assert error_mes == u''
            print('手机号为空，密码不为空 pass.')
        except Exception as e:
            print('手机号为空，密码不为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_d(self):
        """错误的手机号码、密码"""
        login = PowerLogin(self.driver)
        login.power_login_clear()
        time.sleep(2)
        login.power_login_username('13111111111')
        time.sleep(2)
        login.power_login_password('111111')
        time.sleep(2)
        login.power_login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的手机号码、密码 pass.')
        except Exception as e:
            print('错误的手机号码、密码 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_e(self):
        """错误的密码，正确的手机号"""
        login = PowerLogin(self.driver)
        login.power_login_clear()
        time.sleep(2)
        login.power_login_username('15107045860')
        time.sleep(2)
        login.power_login_password('111111')
        time.sleep(2)
        login.power_login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的密码，正确的手机号 pass.')
        except Exception as e:
            print('错误的密码，正确的手机号 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_f(self):
        """错误的手机号，正确的密码"""
        login = PowerLogin(self.driver)
        login.power_login_clear()
        time.sleep(2)
        login.power_login_username('13107045860')
        time.sleep(2)
        login.power_login_password('045860')
        time.sleep(2)
        login.power_login_button()
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的手机号，正确的密码 pass.')
        except Exception as e:
            print('错误的手机号，正确的密码 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_g(self):
        """登录成功"""
        login = PowerLogin(self.driver)
        login.power_login_clear()
        time.sleep(2)
        login.power_login_username('15107045860')
        time.sleep(1)
        login.power_login_password('045860')
        time.sleep(1)
        login.power_login_button()
        time.sleep(2)
        # 断言，登录成功
        error_mes = login.find_element('xpath=>//*[@id="topbar"]/div[1]/a[1]').text  # 基金公司值含1
        try:
            assert error_mes == u'飘飘然'
            print('登录成功 pass.')
        except Exception as e:
            print('登录成功 fail', format(e))
            print(error_mes)
        time.sleep(2)
