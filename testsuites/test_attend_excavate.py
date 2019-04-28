import time
from pageobjects.attend_excavate import AttendExcavate
from testsuites.my_test import MyTest


class TestAttendExcavate(MyTest):
    """投顾挖掘筛选"""

    def test_attend_excavate_case1(self):
        attend = AttendExcavate(self.driver)
        attend.attend_excavate_login()


