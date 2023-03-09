# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/16 21:00
@Auth ： qihang
qq空间登录
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

uesr = '839065235'
pwd = 'xxxx'


def auto_login_qqzone():
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


auto_login_qqzone()
