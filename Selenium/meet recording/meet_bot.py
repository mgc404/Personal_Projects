from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller 
from pynput.keyboard import Key, Controller

# Get google chrom
driver = webdriver.Chrome('D:\Programas\Selenium\chromedriver_win32\chromedriver')
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# entra a la conta de google
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('mateu.garcia@estudiantat.upc.edu')
sleep(0.3)

# Lidiar amb els popups
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(1)

# Iniciar sesio a atenea
driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys('mateu.garcia')
driver.find_element_by_xpath('//*[@id="edit-pass"]').send_keys('Mgc2603+')
driver.find_element_by_xpath('//*[@id="submit_ok"]').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
sleep(2)
driver.get("https://meet.google.com/snm-wstk-wrk")
sleep(1)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()

mouse = mouse.Controller()
# Bloquejo camara i micro
mouse.position = (390, 215)
mouse.click(Button.left, 1)
sleep(0.25)

# Posu pantalla completa el navegador
mouse.position = (1000, 29)

mouse.click(Button.left, 1)
sleep(1)

# Entro al meet
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()

# Començo la grabacio
mouse.position = (1501, 785)
mouse.click(Button.left, 1)

# Posu pantalla completa el meet
mouse.position = (1501, 785)
mouse.click(Button.left, 1)
mouse.position = (1230, 397)
mouse.click(Button.left, 1)
