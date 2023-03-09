# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/16 16:15
@Auth ： qihang
百度网盘登录
"""

from selenium import webdriver
from common.toolSelenium import ToolSelenium
from selenium.webdriver.common.by import By
from time import sleep

user = '18209188798'
pwd = 'xxxxxx'

def baidupan_login():
    driver = webdriver.Chrome()
    client = ToolSelenium(driver)
    client.driver.get('https://pan.baidu.com/')
    sleep(3)

    shown_login_form = ('xpath', 'html/body/section/main/div/section/main/div/div/div[3]/button')
    client.click(shown_login_form)
    sleep(3)
    account = ('id', "TANGRAM__PSP_11__userName")
    password = ('id', "TANGRAM__PSP_11__password")
    client.fill(account, user)
    sleep(3)

    client.fill(password, pwd)
    sleep(3)

    click_obj = ('id', "TANGRAM__PSP_11__submit")
    client.click(click_obj)
    sleep(5)
    client.driver.quit()


def testLogin():
    driver = webdriver.Chrome()

    driver.get('https://pan.baidu.com/')
    sleep(3)

    # 点击去登录
    button = driver.find_element(By.XPATH, "html/body/section/main/div/section/main/div/div/div[3]/button")
    button.click()
    sleep(3)

    userName = driver.find_element(By.ID, "TANGRAM__PSP_11__userName")
    userName.send_keys(user)
    sleep(3)

    password = driver.find_element(By.ID, "TANGRAM__PSP_11__password")
    password.send_keys(pwd)
    sleep(3)

    buttongo = driver.find_element(By.ID, "TANGRAM__PSP_11__submit")
    buttongo.click()
    sleep(3)

    driver.quit()


baidupan_login()
