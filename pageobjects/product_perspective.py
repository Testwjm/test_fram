import time
from framework.base_page import BasePage


class PowerProductPerspective(BasePage):
    """产品透视筛选"""

    screen_publict = 'xpath=>//*[@id="choiceTbl"]/div[1]/ul/li[2]'  # 公募基金

    def product_perspective_public(self):
        self.click(self.screen_publict)
