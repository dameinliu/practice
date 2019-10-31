from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options() # 实例化Option对象
firefox_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式

# 设置引擎为Chrome，在后台默默运行
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe', options = firefox_options)

# driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)


show_all = driver.find_element_by_class_name('comment__show_all').find_element_by_tag_name('a').click()

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')

for comment in comments:
	cmt = comment.find_element_by_tag_name('p')
	print('评论：%s\n ---\n'%cmt.text)

driver.close()
driver.quit()