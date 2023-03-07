# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""

from common.request_tool import RequestTool
import time

import unittest

class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        print("===== setUp =====")

    def tearDown(self) -> None:
        print("===== tearDown =====")

    def test_cc(self):
        driver = RequestTool()
        driver.open_url('https://www.baidu.com/')
        # driver.input_data('id', 'kw', '哈哈')
        driver.find_element('id', 'kw').send_keys('哈哈')
        time.sleep(2)
        # driver.find_element('id', 'su').click()
        driver.click('id', 'su')

        time.sleep(2)
        # driver.get_screenshot(2)
        driver.delete_self()




