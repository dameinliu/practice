# 自动打开网站，填写表单并提交
from selenium import  webdriver
import time

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
terms = input("关键词：")
driver.get('https://www.amazon.com/s?k='+terms) 
time.sleep(2)

