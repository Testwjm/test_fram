import time
from pageobjects.baidu_homepage import HomePage
from testsuites.MyTest import MyTest


class BaiduSearch(MyTest):

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(5)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print("Test Pass.")
        except Exception as e:
            print('Test Fail.', format(e))

    # def test_baidu_search2(self):
    #     homepage = HomePage(self.driver)
    #     homepage.type_search('Python')  # 调用页面对象中的方法
    #     homepage.send_submit_btn()  # 调用页面对象类中点击搜索按钮方法
    #     time.sleep(2)
    #     homepage.get_windows_img()  # 调用基类截图方法
    #     try:
    #         assert 'Python' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
    #         print("Test Pass.")
    #     except Exception as e:
    #         print('Test Fail.', format(e))

