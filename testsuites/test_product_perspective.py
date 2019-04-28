import time
from pageobjects.product_perspective import ProductPerspective
from testsuites.my_test import MyTest


class TestProductPerspective(MyTest):
    """产品透视筛选"""

    def test_product_perspective_case1(self):
        """登录"""
        product = ProductPerspective(self.driver)
        product.product_perspective_login()
        time.sleep(2)

    def test_product_perspective_case2(self):
        product = ProductPerspective(self.driver)
        pass
