import time
from pageobjects.attend_excavate import PowerAttendExcavate
from testsuites.MyTest import MyTest


class FofPowerAttendExcavate(MyTest):
    """投顾挖掘筛选"""

    def attend_excavate_pass(self):
        attend = PowerAttendExcavate(self.driver)
        attend.attend_excavate_pass()
