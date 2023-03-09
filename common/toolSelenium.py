# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/9
@Auth ： qihang
基于Selenium的操作封装类。
"""

# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class ToolSelenium:
    def __init__(self, driver):
        self.driver = driver

    # 查找指定定位的元素
    def find(self, locator):
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    # 填充文本到指定的文本元素
    def fill(self, locator, text):
        self.find(locator).send_keys(text)

    # 判断对象是否存在
    def element_exists(self, locator) -> bool:
        ones = self.find(locator)
        if len(ones) > 1:
            return True
        else:
            return False

    # 单击
    def click(self, locator):
        self.find(locator).click()
