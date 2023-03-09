# -*- coding: utf-8 -*-
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 访问腾讯首页
driver.get('https://www.qq.com')

# 获得当前窗口
nowhandle = driver.current_window_handle

# 打开新窗口(新闻)
driver.find_element(By.CSS_SELECTOR, "[bosszone=dh_1]").click()

time.sleep(3)
# 获取所有窗口
all_handles = driver.window_handles

for handle in all_handles:
    if handle != nowhandle:
        print("need to switch to nowhandle")
        driver.switch_to.window(handle)
        time.sleep(3)

cc = driver.find_element(By.XPATH, '//*[@id="List"]/div/div[1]/div/span[1]')
print(cc.text)

driver.quit()
