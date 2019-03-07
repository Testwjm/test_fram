import time
from pageobjects.power_login import FofPowerLogin
from testsuites.MyTest import MyTest


class PowerLogin(MyTest):

    def test_power_search(self):
        login = FofPowerLogin(self.driver)
        login.type_power_search()
        time.sleep(3)
        login.input_power_username("15107045860")
        time.sleep(1)
        login.input_power_password("123456wang")
        time.sleep(1)
        login.search_power_submit()
        time.sleep(5)
        try:
            assert '首页' in login.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print("Test Pass.")
        except Exception as e:
            login.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))
        time.sleep(3)


