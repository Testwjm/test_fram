from pageobjects.baidu_homepage import HomePage
from testsuites.MyTest import MyTest


class GetPageTitle(MyTest):

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())

