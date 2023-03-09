# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MouseOperator:
    def __init__(self, driver):
        self.driver = driver

    # 处理双击事件
    def double_click(self, locator):
        # 定位到要双击的元素
        double = self.driver.find_element(By.XPATH, locator)
        # 对定位到的元素执行鼠标双击操作
        ActionChains(self.driver).double_click(double).perform()

    # 处理鼠标右键
    def right_click(self, locator):
        # 定位到要右击的元素
        right = self.driver.find_element(By.XPATH, locator)
        # 对定位到的元素执行鼠标右键操作
        ActionChains(self.driver).context_click(right).perform()

    # 处理拖放元素
    def drag_drop(self, source_locator, target_locator):
        # 定位元素的原位置
        element = self.driver.find_element(By.XPATH, source_locator)
        # 定位元素要移动到的目标位置
        target = self.driver.find_element(By.XPATH, target_locator)
        # 执行元素的移动操作
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def hover_one_element(self, locator):
        # 定位到鼠标移动到上面的元素
        above = self.driver.find_element(By.XPATH, locator)
        # 对定位到的元素执行鼠标移动到上面的操作
        ActionChains(self.driver).move_to_element(above).perform()

    def left_click_hover(self, locator):
        # 定位到鼠标按下左键的元素
        left = self.driver.find_element(By.XPATH, locator)
        # 对定位到的元素执行鼠标左键按下的操作
        ActionChains(self.driver).click_and_hold(left).perform()
