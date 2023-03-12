# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""
from common.request_tool import RequestTool
from common.read_config import ReadConfig
import time
import unittest
import requests
from common.HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
import os


class TestBaiDu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("对象执行前")

    @classmethod
    def tearDownClass(cls):
        print("对象执行后")

    # 做初始化
    def setUp(self) -> None:
        print("===== setUp =====")
        self.url = "https://www.baidu.com/"

    # 做清理
    def tearDown(self) -> None:
        print("===== tearDown =====")

    def test_search1(self):
        print("test_search1")

        data = "哈哈1"
        r = requests.get(self.url, data)
        self.assertEqual(r.status_code, 200)

    def test_search2(self):
        print("test_search2")

        data = "百度"
        r = requests.get(self.url, data)
        self.assertEqual(r.status_code, 200)

    def test_search3(self):
        print("test_search3")
        driver = RequestTool()
        ipconfig = ReadConfig().get_http('baseurl')

        driver.open_url(ipconfig)
        driver.find_element('id', 'kw').send_keys('哈哈2')
        time.sleep(2)
        driver.click('id', 'su')

        time.sleep(2)
        driver.get_screenshot(2)
        driver.delete_self()


# 测试套件
def my_suite():
    mysuite = unittest.TestSuite()
    mysuite.addTest(TestBaiDu("test_search1"))
    return mysuite


if __name__ == "__main__":
    # 仅执行套件部分
    # test = unittest.TextTestRunner()
    # test.run(my_suite())

    # 全部执行
    # unittest.main()

    # 以HTMLTestRunner生成报告
    # fr = open("res.html", "wb")
    # runner = HTMLTestRunner(stream=fr, title="测试报告", description="详情")
    # runner.run(my_suite())
    # fr.close()  # 关闭报告文件

    # 以HTMLTestRunner生成报告
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    filename = now + '.html'

    # 加载执行用例生成报告
    result = BeautifulReport(my_suite())

    # 定义报告属性
    result.report(description='测试报告', filename=filename, theme='theme_default')
