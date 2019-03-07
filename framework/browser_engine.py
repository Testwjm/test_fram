import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger


logger = Logger(logger="BrowserEngine").get_log()


class BrowserEngine(object):

    def open_browser(self):
        # 读取配置文件
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        # 读取配置文件里定义的browser和url并打印日志
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Chrome":
            dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
            chrome_driver_path = dir + '/tools/chromedriver.exe'
            driver = webdriver.Chrome(chrome_driver_path)
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
        logger.info("Starting %s browser." % browser)  # 打印使用的浏览器

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()  # 最大化浏览器
        logger.info("最大化浏览器")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    @staticmethod
    def quit_browser(driver):
        logger.info("关闭浏览器")
        driver.quit()  # 关闭浏览器


# test
'''
browser = BrowserEngine()
driver = browser.open_browser()
browser.quit_browser(driver)
'''
