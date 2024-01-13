import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
url = 'https://www.baidu.com/'
driver.get(url)
driver.find_element_by_id('kw').send_keys('吉利大厦')
driver.find_element_by_id('su').click()
time.sleep(2)
js = "window.scrollTo(0, 2000)"
driver.execute_script(js)
driver.close()