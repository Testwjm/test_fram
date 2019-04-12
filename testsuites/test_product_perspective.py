import time
from pageobjects.product_perspective import PowerProductPerspective
from testsuites.MyTest import MyTest


class FofPowerProductPerspective(MyTest):
    """产品透视筛选"""

    def test_product_perspective_a(self):
        product = PowerProductPerspective(self.driver)
        product.product_perspective_public()
        time.sleep(2)
