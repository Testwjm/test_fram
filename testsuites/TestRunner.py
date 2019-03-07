import unittest
import time
import os
# from HTMLTestRunner import HTMLTestRunner

# 设置报告文件保存路径
report_path = os.path.abspath('..') + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTML_template.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.defaultTestLoader.discover('./', pattern="test_*.py")  # 加载当前目录整个包下所有测试用例

# suite = unittest.TestSuite()
# suite.addTest(GetPageTitle('test_get_title'))  # 加载一个单独的测试用例
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))  # 加载一个类下所有的测试用例


if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)

