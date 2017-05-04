# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://www.baidu.com/")

browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
sleep(1000000)

browser.quit()
