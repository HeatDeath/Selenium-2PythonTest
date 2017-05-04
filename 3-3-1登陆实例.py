# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"

driver.get(url)
# driver.find_element_by_css_selector("#u1 > a[name=tj_login]").click()
# #TANGRAM__PSP_3__userName
driver.find_element_by_css_selector("#TANGRAM__PSP_3__userName").clear()
driver.find_element_by_css_selector("#TANGRAM__PSP_3__userName").send_keys('userName')
# #TANGRAM__PSP_3__password
driver.find_element_by_css_selector("#TANGRAM__PSP_3__password").clear()
driver.find_element_by_css_selector("#TANGRAM__PSP_3__password").send_keys('password')
# #TANGRAM__PSP_3__submit
driver.find_element_by_css_selector("#TANGRAM__PSP_3__submit").click()

sleep(100000)
driver.quit()

