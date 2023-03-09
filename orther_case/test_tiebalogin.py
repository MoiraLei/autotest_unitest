# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

user = '18209188798'
pwd = 'xxxxxx'

def tieba_login():
    driver = webdriver.Chrome()
    driver.get('https://tieba.baidu.com/index.html')
    # 点击登录链接
    first_btn = driver.find_element(By.CSS_SELECTOR, "#com_userbar > ul > li.u_login > div > a")

    first_btn.click()

    time.sleep(3)
    # 点击【用户名登录】选项
    show_account_login = driver.find_element(By.ID, 'TANGRAM__PSP_4__footerULoginBtn')
    show_account_login.click()
    time.sleep(2)
    # 填充账号和密码
    driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys(user)
    time.sleep(2)
    driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys(pwd)

    time.sleep(2)

    driver.find_element(By.ID, 'TANGRAM__PSP_4__submit').click()

    time.sleep(5)
    driver.quit()


tieba_login()