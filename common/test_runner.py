# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""

import time, os
import unittest
from common.HTMLTestRunner import HTMLTestRunner
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class TestRunner(object):
    ''' 执行测试用例 '''

    def __init__(self, cases="../test_case/", title="Auto Test Report", description="Test case execution"):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):
        # 标记文件夹reports是否存在
        has_reports = False
        for filename in os.listdir(project_dir):
            if filename == "reports":
                has_reports = True
                break
        if has_reports is False:
            os.mkdir(project_dir + '/reports')
        now = time.strftime("%Y-%m-%d_%H_%M_%S")

        fp = open(project_dir + "/reports/" + now + "result.html", 'w')

        tests = unittest.defaultTestLoader.discover(start_dir=self.cases, pattern='test*.py')
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()
