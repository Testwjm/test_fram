# unittest测试框架
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner


# 设置报告文件保存路径
report_path = os.path.abspath('..') + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTML_template.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.defaultTestLoader.discover('./', pattern="test_*.py")  # 加载当前目录整个包下所有测试用例

if __name__ == '__main__':

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件

