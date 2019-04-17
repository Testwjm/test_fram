import time
from pageobjects.attend_excavate import AttendExcavate
from testsuites.MyTest import MyTest


class TestAttendExcavate(MyTest):
    """投顾挖掘筛选"""

    def test_attend_excavate_alogin(self):
        attend = AttendExcavate(self.driver)
        attend.attend_excavate_login()


