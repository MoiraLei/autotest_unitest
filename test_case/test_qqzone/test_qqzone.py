# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/16 21:00
@Auth ： qihang
使用selenium进行qq空间登录
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

uesr = '839065235'
pwd = 'xxxx'


class TestQQ(unittest.TestCase):

    def test_login_qqzone(self):
        driver = webdriver.Chrome()
        driver.set_window_position(20, 40)
        driver.set_window_size(1100, 700)

        driver.get("http://qzone.qq.com")
        sleep(1)
        driver.switch_to.frame('login_frame')
        # driver.switch_to.('login_frame')
        # driver.find_element(By.ID, "login_frame").click()

        driver.find_element(By.ID, "switcher_plogin").click()
        sleep(1)

        driver.find_element(By.ID, "u").send_keys(uesr)
        sleep(1)

        driver.find_element(By.ID, "p").send_keys(pwd)
        sleep(1)

        driver.find_element(By.ID, "login_button").click()
        sleep(5)

        driver.quit()

