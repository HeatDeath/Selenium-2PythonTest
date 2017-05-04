# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

print("设置浏览器 480宽， 800高显示")
driver.set_window_size(480, 800)
sleep(100000)
driver.quit()
