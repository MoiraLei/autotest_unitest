# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/7
@Auth ： qihang
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os


class RequestTool(object):
    __project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def find_element(self, element_type, value):
        if element_type == 'id':
            el = self.driver.find_element(By.ID, value)
        if element_type == 'name':
            el = self.driver.find_element(By.NAME, value)
        if element_type == 'class_name':
            el = self.driver.find_element(By.CLASS_NAME, value)
        if element_type == 'tag_name':
            el = self.driver.find_element(By.TAG_NAME, value)
        if element_type == 'link':
            el = self.driver.find_element(By.LINK_TEXT, value)
        if element_type == 'css':
            el = self.driver.find_element(By.CSS_SELECTOR, value)
        if element_type == 'partial_link':
            el = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        if element_type == 'xpath':
            el = self.driver.find_element(By.XPATH, value)
        if el:
            return el
        else:
            return None

    # 利用Selenium的点击事件
    def click(self, element_type, value):
        self.find_element(element_type, value).click()

    # 利用Selenium输入
    def input_data(self, element_type, value, data):
        self.find_element(element_type, value).send_keys(data)

    # 获取截图
    def get_screenshot(self, id):
        # 标记文件夹picture是否存在
        has_picture = False
        for filename in os.listdir(os.path.dirname(os.getcwd())):
            if filename == 'picture':
                has_picture = True
                break
            # else:
            #     print(filename)
        if has_picture is False:
            os.mkdir(os.path.dirname(os.getcwd()) + '/picture/')
        photo = self.driver.get_screenshot_as_file(
            self.__project_dir + '/picture/' + str(id) + str('_') + time.strftime("%Y-%m-%d-%H-%M-%S") + '.png')
        return photo

    def delete_self(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


# if __name__ == '__main__':
#     driver = RequestTool()
#     driver.open_url('https://www.baidu.com/')
#     # driver.input_data('id', 'kw', '哈哈')
#     driver.find_element('id', 'kw').send_keys('哈哈')
#     time.sleep(2)
#     # driver.find_element('id', 'su').click()
#     driver.click('id', 'su')
#
#     time.sleep(2)
#     driver.get_screenshot(1)
#     driver.delete_self()
