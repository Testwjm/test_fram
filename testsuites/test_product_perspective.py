import time
from pageobjects.product_perspective import ProductPerspective
from testsuites.MyTest import MyTest


class TestProductPerspective(MyTest):
    """产品透视筛选"""

    def test_product_perspective_alogin(self):
        product = ProductPerspective(self.driver)
        product.product_perspective_login()
        time.sleep(2)
