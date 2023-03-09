# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/9
@Auth ： qihang
使用splinter登录163邮箱
安装： pip install splinter
"""

import time
from splinter import Browser

user = 'lllgou2021@yeah.net'
pwd = 'xxxxxxxxx'


def login_mail(url):
    browser = Browser('chrome')
    browser.visit(url)

    # 等待加载
    time.sleep(3)
    # 点击登录按钮
    browser.find_by_xpath("//div[@id='app']//div//div//div//div//div//div[2]/div[2]/div").click()
    # 切换frame
    browser.driver.switch_to.frame(0)
    # 判断登录邮箱组件是否已经加载出来
    aa = browser.is_element_present_by_xpath("//input[@name='email']")
    if aa:
        # fill in account and password
        browser.find_by_xpath("//input[@name='email']").fill(user)
        browser.find_by_xpath("//input[@name='password']").fill(pwd)
        time.sleep(3)
        # click the button of login
        browser.find_by_id('dologin').click()
        time.sleep(10)
    else:
        print('邮箱组件未加载出来')
    # close the window of brower
    browser.quit()


if __name__ == '__main__':
    mail_addr = 'http://reg.163.com/'
    login_mail(mail_addr)
