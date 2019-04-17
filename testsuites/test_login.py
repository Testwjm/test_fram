import time
from pageobjects.login import Login
from testsuites.MyTest import MyTest


class TestLogin(MyTest):
    """登录"""

    def test_login_atest(self):
        """手机号、密码为空"""
        login = Login(self.driver)
        login.login_homepage()
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="userName"]').text
        try:
            assert error_mes == u''
            print('手机号、密码为空 pass.')
        except Exception as e:
            print('手机号、密码为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_btest(self):
        """密码为空，手机号不为空"""
        login = Login(self.driver)
        login.login_username('15107045860')
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="password"]').text
        try:
            assert error_mes == u''
            print('密码为空，手机号不为空 pass.')
        except Exception as e:
            print('密码为空，手机号不为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_ctest(self):
        """手机号为空，密码不为空"""
        login = Login(self.driver)
        login.login_clear()
        time.sleep(2)
        login.login_password('045860')
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="userName"]').text
        try:
            assert error_mes == u''
            print('手机号为空，密码不为空 pass.')
        except Exception as e:
            print('手机号为空，密码不为空 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_dtest(self):
        """错误的手机号码、密码"""
        login = Login(self.driver)
        login.login_clear()
        time.sleep(2)
        login.login_username('13111111111')
        time.sleep(2)
        login.login_password('111111')
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的手机号码、密码 pass.')
        except Exception as e:
            print('错误的手机号码、密码 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_etest(self):
        """错误的密码，正确的手机号"""
        login = Login(self.driver)
        login.login_clear()
        time.sleep(2)
        login.login_username('15107045860')
        time.sleep(2)
        login.login_password('111111')
        time.sleep(2)
        login.login_button()
        time.sleep(2)
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的密码，正确的手机号 pass.')
        except Exception as e:
            print('错误的密码，正确的手机号 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_ftest(self):
        """错误的手机号，正确的密码"""
        login = Login(self.driver)
        login.login_clear()
        time.sleep(2)
        login.login_username('13107045860')
        time.sleep(2)
        login.login_password('045860')
        time.sleep(2)
        login.login_button()
        error_mes = login.find_element('xpath=>//*[@id="btnSubmit"]/span').text
        try:
            assert error_mes == u'登录'
            print('错误的手机号，正确的密码 pass.')
        except Exception as e:
            print('错误的手机号，正确的密码 fail', format(e))
            print(error_mes)
        time.sleep(2)

    def test_login_gtest(self):
        """登录成功"""
        login = Login(self.driver)
        login.login_clear()
        time.sleep(2)
        login.login_username('15107045860')
        time.sleep(1)
        login.login_password('045860')
        time.sleep(1)
        login.login_button()
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
