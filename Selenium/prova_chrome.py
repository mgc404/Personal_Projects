from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\Programas\Selenium\chromedriver_win32\chromedriver.exe')

driver.get('https://www.youtube.com/?hl=es&gl=ES')
input()
##driver.find_element_by_xpath('//*[@id="button"]').click()

driver.find_element_by_xpath('//*[@id="search"]').send_keys('muzska')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)

